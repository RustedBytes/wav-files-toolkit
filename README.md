# wav-files-toolkit

- [x] All binaries in one archive to work with WAV files
- [x] Rust-based, with test suits
- [ ] Binaries are *statically-linked*

## Tools

- [ ] [wav-files-**convert**](https://github.com/RustedBytes/wav-files-convert): Convert between WAV and other formats (MP3, FLAC)
- [x] [wav-files-**augment**](https://github.com/RustedBytes/wav-files-augment): Create modified audio by adding noise, shifting pitch for WAV files
- [x] [wav-files-**spectrogram**](https://github.com/RustedBytes/wav-files-spectrogram): Generate visual spectrogram images from audio for WAV files
- [x] [wav-files-**normalize**](https://github.com/RustedBytes/wav-files-normalize): Adjust audio to a target peak or integrated loudness (LUFS) of WAV files
- [x] [wav-files-**format**](https://github.com/RustedBytes/wav-files-format): Standardize sample rate, bit depth, and channels of WAV files
- [x] [wav-files-**validate**](https://github.com/RustedBytes/wav-files-validate): Validate file integrity of WAV files in a folder
- [x] [wav-files-**concat**](https://github.com/RustedBytes/wav-files-concat): Concatenate audio files into one file
- [x] [wav-files-**chunker**](https://github.com/RustedBytes/wav-files-chunker): Chunk WAV files into smaller pieces
- [x] [wav-files-**ss**](https://github.com/RustedBytes/wav-files-ss): Speech Separation (using WebRTC VAD) for WAV files
- [x] [wav-files-**filter**](https://github.com/RustedBytes/wav-files-filter): Filter audios by their length
- [x] [wav-files-**stats**](https://github.com/RustedBytes/wav-files-stats): Calculate statistics of a folder with WAV files

### TODO

<details>

  <summary>Good next programs to implement</summary>
  
- [ ] wav-files-**denoise**: Apply noise reduction algorithms (e.g., spectral subtraction or Wiener filtering) to remove background noise from WAV files. Why? Complements augmentation (which adds noise) by enabling cleanup; essential for real-world recordings.
- [ ] wav-files-**eq**: Apply equalization filters to boost/cut specific frequency bands in WAV files. Why? Builds on spectrogram visualization for targeted audio shaping; useful for mastering or voice enhancement.
- [ ] wav-files-**trim**: Automatically detect and trim silence from the start/end of WAV files, with optional threshold settings. Why? Enhances speech separation and chunking by removing dead air; streamlines podcast or interview processing.
- [ ] wav-files-**compress**: Apply dynamic range compression to even out loud/soft parts in WAV files, with adjustable ratio/threshold. Why? Pairs with normalization for professional loudness control; prevents clipping in mixed or concatenated files.
- [ ] wav-files-**tempo**: Adjust playback speed/tempo of WAV files without altering pitch (using time-stretching algorithms like WSOLA). Why? Extends pitch-shifting augmentation to rhythm; great for music remixing or sped-up training data.
- [ ] wav-files-**metadata**: Edit or extract embedded metadata (e.g., artist, title, comments) in WAV files using RIFF chunks. Why? Fills a gap in file handling; integrates with stats and validation for better organization in folders.
- [ ] wav-files-**waveform**: Generate static waveform plot images (PNG/SVG) from WAV files, with customizable styles. Why? Expands visualization beyond spectrograms; quick for previews or reports alongside stats.
- [ ] wav-files-**mix**: Overlay or blend multiple WAV files into a single output, with volume balancing and channel mapping (e.g., stereo mixdown). Why? Extends concatenation for layered audio (e.g., voiceover on music); useful for post-production without full DAWs.
- [ ] wav-files-**echo**: Add echo, reverb, or chorus effects to WAV files using delay-based DSP parameters (e.g., decay time, wet/dry mix). Why? Enhances augmentation with spatial effects; great for simulating environments in voice recordings.
- [ ] wav-files-**fft**: Compute and export Fast Fourier Transform (FFT) data as text/CSV for frequency analysis of WAV files. Why? Deeper dive beyond spectrograms for quantitative spectral insights; supports research or automated quality checks.

</details>

## Authors

- Yehor Smoliakov (contact: <egorsmkv@gmail.com>)
