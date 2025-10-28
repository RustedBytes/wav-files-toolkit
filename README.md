# wav-files-toolkit

[![build](https://github.com/RustedBytes/wav-files-toolkit/actions/workflows/download-and-release.yml/badge.svg)](https://github.com/RustedBytes/wav-files-toolkit/actions/workflows/download-and-release.yml)

- [x] Rust-based, with test suites
- [x] Binaries are *statically-linked*

Download the latest archive from [the Releases page](https://github.com/RustedBytes/wav-files-toolkit/releases).

## Tools

- [x] [wav-files-**convert**](https://github.com/RustedBytes/wav-files-convert): Convert MP3, FLAC, OGG, M4A, AAC, WMA, AIFF, AU, MP2 to WAV
- [x] [wav-files-**augment**](https://github.com/RustedBytes/wav-files-augment): Create modified audio by adding noise, shifting pitch for WAV files
- [x] [wav-files-**spectrogram**](https://github.com/RustedBytes/wav-files-spectrogram): Generate visual spectrogram images from audio for WAV files
- [x] [wav-files-**normalize**](https://github.com/RustedBytes/wav-files-normalize): Adjust audio to a target peak or integrated loudness (LUFS) of WAV files
- [x] [wav-files-**format**](https://github.com/RustedBytes/wav-files-format): Standardize sample rate, bit depth, and channels of WAV files
- [x] [wav-files-**validate**](https://github.com/RustedBytes/wav-files-validate): Validate file integrity of WAV files in a folder
- [x] [wav-files-**concat**](https://github.com/RustedBytes/wav-files-concat): Concatenate audio files into one file
- [x] [wav-files-**chunker**](https://github.com/RustedBytes/wav-files-chunker): Chunk WAV files into smaller pieces
- [x] [wav-files-**vad**](https://github.com/RustedBytes/wav-files-vad): Extract speech using WebRTC VAD for WAV files
- [x] [wav-files-**vad-api**](https://github.com/RustedBytes/wav-files-vad-api): Extract speech using an API that performs Voice Speech Detection for WAV files
- [x] [wav-files-**filter**](https://github.com/RustedBytes/wav-files-filter): Filter audios by their length
- [x] [wav-files-**stats**](https://github.com/RustedBytes/wav-files-stats): Calculate statistics of a folder with WAV files
- [x] [wav-files-**trim**](https://github.com/RustedBytes/wav-files-trim): Automatically detect and trim silence from the start/end of WAV files, with optional threshold settings
- [x] [wav-files-**denoise**](https://github.com/RustedBytes/wav-files-denoise): Apply noise reduction tool [*nnnoiseless*](https://github.com/jneem/nnnoiseless) to remove background noise from WAV files
- [x] [wav-files-**denoise-api**](https://github.com/RustedBytes/wav-files-denoise-api): Apply noise reduction API to remove background noise from WAV files
- [x] [wav-files-**tempo**](https://github.com/RustedBytes/wav-files-tempo): Adjust playback speed/tempo of WAV files without altering pitch (using time-stretching algorithms like WSOLA)
- [x] [wav-files-**echo**](https://github.com/RustedBytes/wav-files-echo): Add echo, reverb, or chorus effects to WAV files using delay-based DSP parameters (e.g., decay time, wet/dry mix)

## Additional Tools

The following tools are available in the `additional-tools.zip` release archive:

- [x] [**audios-to-dataset**](https://github.com/RustedBytes/audios-to-dataset): Convert audio files to dataset format
- [x] [**extract-audio**](https://github.com/RustedBytes/extract-audio): Extract audio from various sources
- [x] [**babylonify**](https://github.com/RustedBytes/babylonify): Filter parquet files by language

## 3rd-party Tools

The following external tools are bundled with the toolkit and available in the `3d-party-bins.zip` release archive:

- [x] [**FFmpeg**](https://ffmpeg.org/): A complete, cross-platform solution to record, convert and stream audio and video (static build from [johnvansickle.com](https://johnvansickle.com/ffmpeg/))
- [x] [**ffprobe**](https://ffmpeg.org/ffprobe.html): Multimedia stream analyzer, included with FFmpeg
- [x] [**parquet-tools**](https://github.com/hangxie/parquet-tools): Command-line tools for Apache Parquet files
- [x] [**nnnoiseless**](https://github.com/RustedBytes/nnnoiseless-releases): RNNoise-based noise suppression tool
- [x] [**audio-from-video**](https://github.com/RustedBytes/audio-from-video): Extract audio tracks from video files
- [x] [**data-viewer-audio**](https://github.com/RustedBytes/data-viewer-audio): View and inspect audio dataset information
- [x] [**audio-parquet-merger**](https://github.com/RustedBytes/audio-parquet-merger): Merge multiple audio parquet files

### Demo

- https://colab.research.google.com/drive/1iVqnDZLYi6Dz_pUda10WP4DeDrJwugMc?usp=sharing

### Good next programs to implement

<details>

  <summary>Open the list</summary>
  
- [ ] wav-files-**eq**: Apply equalization filters to boost/cut specific frequency bands in WAV files. Why? Builds on spectrogram visualization for targeted audio shaping; useful for mastering or voice enhancement.
- [ ] wav-files-**compress**: Apply dynamic range compression to even out loud/soft parts in WAV files, with adjustable ratio/threshold. Why? Pairs with normalization for professional loudness control; prevents clipping in mixed or concatenated files.
- [ ] wav-files-**metadata**: Edit or extract embedded metadata (e.g., artist, title, comments) in WAV files using RIFF chunks. Why? Fills a gap in file handling; integrates with stats and validation for better organization in folders.
- [ ] wav-files-**waveform**: Generate static waveform plot images (PNG/SVG) from WAV files, with customizable styles. Why? Expands visualization beyond spectrograms; quick for previews or reports alongside stats.
- [ ] wav-files-**fft**: Compute and export Fast Fourier Transform (FFT) data as text/CSV for frequency analysis of WAV files. Why? Deeper dive beyond spectrograms for quantitative spectral insights; supports research or automated quality checks.
- [ ] wav-files-**mix**: Overlay or blend multiple WAV files into a single output, with volume balancing and channel mapping (e.g., stereo mixdown)
- [ ] wav-files-**volume**: Adjust overall gain or apply random volume scaling (e.g., ±dB range) to WAV files for dynamic loudness variation. Why for ML? Simulates real-world recording inconsistencies (e.g., microphone distance); pairs with normalization to prevent overfitting in tasks like speaker identification, boosting generalization as seen in torchaudio pipelines.
- [ ] wav-files-**shift**: Perform time-domain shifting by inserting silence or cropping edges to offset audio start/end randomly. Why for ML? Introduces temporal misalignment common in streaming audio; essential for sequence models (e.g., RNNs/LSTMs) in event detection, reducing sensitivity to exact timing as in raw waveform augmentations.
- [ ] wav-files-**crop**: Extract fixed-length random segments (with overlap options) from longer WAV files. Why for ML? Generates variable-length clips for balanced batching in training; critical for fixed-input models like CNNs on audio spectrograms, mimicking dataset imbalances in environmental sound classification.
- [ ] wav-files-**mask**: Apply time-domain masking by zeroing out random contiguous segments (e.g., SpecAugment-inspired on waveform). Why for ML? Encourages models to focus on partial signals, enhancing robustness to occlusions; useful for bioacoustics or music tagging where partial data is common, as in masking strategies for DL.
- [ ] wav-files-**channel**: Swap, drop, or mix stereo channels (e.g., mono conversion with panning) for multi-channel WAV files. Why for ML? Handles channel imbalances in stereo datasets; augments for mono-compatible models, aiding transfer learning in spatial audio tasks like source separation.

</details>

## Authors

- Yehor Smoliakov (contact: <egorsmkv@gmail.com>)

## Cite

```
@software{Smoliakov_Wav_Files_Toolkit,
  author = {Smoliakov, Yehor},
  month = oct,
  title = {{WAV Files Toolkit: A suite of command-line tools for common WAV audio processing tasks, including conversion from other formats, data augmentation, loudness normalization, spectrogram generation, and validation.}},
  url = {https://github.com/RustedBytes/wav-files-toolkit},
  version = {0.4.0},
  year = {2025}
}
```
