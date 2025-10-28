#!/usr/bin/env python3
"""
Script to check the latest versions of included programs from their GitHub repositories.
Parses README.md to extract GitHub repository URLs and fetches their latest release information.
Can also check repositories from the GitHub Actions workflow file.
"""

import re
import sys
import urllib.request
import json
from typing import List, Tuple, Optional
import argparse
import time


def extract_github_repos_from_readme(readme_path: str) -> List[Tuple[str, str]]:
    """
    Extract GitHub repository URLs from README.md.
    
    Args:
        readme_path: Path to README.md file
        
    Returns:
        List of tuples (repo_name, repo_url)
    """
    repos = []
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all GitHub repository URLs in the format https://github.com/owner/repo
        pattern = r'\[([^\]]+)\]\((https://github\.com/[^/]+/[^/\)]+)\)'
        matches = re.findall(pattern, content)
        
        for name, url in matches:
            # Clean up the URL (remove any anchors or extra parts)
            url = url.split('#')[0].split('?')[0]
            
            # Skip URLs that don't look like actual repositories
            if any(skip in url for skip in ['/releases', '/actions', '/badge.svg', '.png', '.jpg']):
                continue
                
            # Skip the main repository itself (but not sub-paths)
            if url.endswith('wav-files-toolkit') or url.endswith('wav-files-toolkit/'):
                continue
                
            repos.append((name, url))
    
    except Exception as e:
        print(f"Error reading README: {e}", file=sys.stderr)
        sys.exit(1)
    
    return repos


def extract_github_repos_from_workflow(workflow_path: str) -> List[Tuple[str, str]]:
    """
    Extract GitHub repository URLs from a workflow file.
    
    Args:
        workflow_path: Path to workflow YAML file
        
    Returns:
        List of tuples (repo_name, repo_url)
    """
    repos = []
    
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all GitHub repository URLs
        pattern = r'https://github\.com/([^/]+)/([^/"\s]+)'
        matches = re.findall(pattern, content)
        
        seen = set()
        for owner, repo in matches:
            url = f"https://github.com/{owner}/{repo}"
            
            # Remove any version tags or file extensions
            url = re.sub(r'/releases/.*$', '', url)
            
            if url not in seen:
                seen.add(url)
                repos.append((repo, url))
    
    except Exception as e:
        print(f"Error reading workflow: {e}", file=sys.stderr)
        return []
    
    return repos


def get_latest_release_from_html(repo_url: str, max_retries: int = 2) -> Optional[dict]:
    """
    Scrape the latest release information from GitHub repository's releases page.
    
    Args:
        repo_url: GitHub repository URL (e.g., https://github.com/owner/repo)
        max_retries: Maximum number of retry attempts for failed requests
        
    Returns:
        Dictionary with release information or None if not found
    """
    try:
        # Extract owner and repo name from URL
        parts = repo_url.rstrip('/').split('/')
        if len(parts) < 2:
            return None
            
        owner = parts[-2]
        repo = parts[-1]
        
        # Try to fetch the releases page with retries
        releases_url = f"https://github.com/{owner}/{repo}/releases/latest"
        
        for attempt in range(max_retries + 1):
            try:
                req = urllib.request.Request(releases_url)
                req.add_header('User-Agent', 'Mozilla/5.0 (compatible; version-checker)')
                
                with urllib.request.urlopen(req, timeout=10) as response:
                    html = response.read().decode('utf-8')
                    final_url = response.geturl()
                    
                # Extract version from the final URL after redirect
                # Format: https://github.com/owner/repo/releases/tag/v1.0.0
                version_match = re.search(r'/releases/tag/([^"\']+)', final_url)
                if version_match:
                    version = version_match.group(1)
                    
                    # Try to extract the publish date from HTML
                    date_match = re.search(r'datetime="([^"]+)"', html)
                    published = date_match.group(1).split('T')[0] if date_match else 'N/A'
                    
                    return {
                        'tag_name': version,
                        'published_at': published,
                        'html_url': final_url
                    }
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    return {'error': 'No releases found'}
                elif attempt < max_retries:
                    time.sleep(1)  # Brief pause before retry
                    continue
                else:
                    return {'error': f'HTTP error {e.code}'}
            except (urllib.error.URLError, TimeoutError) as e:
                if attempt < max_retries:
                    time.sleep(1)  # Brief pause before retry
                    continue
                else:
                    return {'error': 'Network error'}
                    
    except Exception as e:
        return {'error': str(e)}
    
    return None


def get_latest_release(repo_url: str) -> Optional[dict]:
    """
    Fetch the latest release information from a GitHub repository.
    Uses web scraping as fallback when API is not available.
    
    Args:
        repo_url: GitHub repository URL (e.g., https://github.com/owner/repo)
        
    Returns:
        Dictionary with release information or None if not found
    """
    # Try HTML scraping approach
    return get_latest_release_from_html(repo_url)


def main():
    """Main function to check versions of all included programs."""
    parser = argparse.ArgumentParser(
        description='Check latest versions of included programs from their GitHub repositories.'
    )
    parser.add_argument(
        '--include-workflow',
        action='store_true',
        help='Also check repositories from the GitHub Actions workflow file'
    )
    
    args = parser.parse_args()
    
    readme_path = 'README.md'
    workflow_path = '.github/workflows/download-and-release.yml'
    
    print("Checking latest versions of included programs...\n")
    
    # Extract repositories from README
    repos = extract_github_repos_from_readme(readme_path)
    
    # Optionally add repos from workflow
    if args.include_workflow:
        workflow_repos = extract_github_repos_from_workflow(workflow_path)
        # Merge, avoiding duplicates
        existing_urls = {url for _, url in repos}
        for name, url in workflow_repos:
            if url not in existing_urls:
                repos.append((name, url))
                existing_urls.add(url)
    
    if not repos:
        print("No GitHub repositories found")
        return
    
    # Filter to only include tool repositories (wav-files-* and related tools)
    tool_repos = []
    for name, url in repos:
        # Include wav-files-* repos and related RustedBytes tools
        if 'wav-files-' in url or ('RustedBytes' in url and 'wav-files-toolkit' not in url):
            tool_repos.append((name, url))
    
    if not tool_repos:
        print("No tool repositories found")
        return
    
    # Remove duplicates
    seen_urls = set()
    unique_repos = []
    for name, url in tool_repos:
        if url not in seen_urls:
            seen_urls.add(url)
            unique_repos.append((name, url))
    
    # Check each repository for latest release
    results = []
    for name, url in unique_repos:
        release_info = get_latest_release(url)
        results.append((name, url, release_info))
    
    # Display results
    print(f"{'Repository':<40} {'Latest Version':<20} {'Published':<25}")
    print("=" * 90)
    
    for name, url, info in results:
        repo_name = url.split('/')[-1]
        
        if info and 'error' not in info:
            version = info['tag_name']
            published = info['published_at'] if info['published_at'] != 'N/A' else 'N/A'
            print(f"{repo_name:<40} {version:<20} {published:<25}")
        elif info and 'error' in info:
            print(f"{repo_name:<40} {'ERROR':<20} {info['error']:<25}")
        else:
            print(f"{repo_name:<40} {'N/A':<20} {'N/A':<25}")
    
    print(f"\n✓ Version check complete! Found {len(results)} repositories.")


if __name__ == '__main__':
    main()
