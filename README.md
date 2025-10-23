# wav-files-toolkit

- [x] Rust-based, with test suits
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
- [x] [wav-files-**ss**](https://github.com/RustedBytes/wav-files-ss): Speech Separation (using WebRTC VAD) for WAV files
- [x] [wav-files-**filter**](https://github.com/RustedBytes/wav-files-filter): Filter audios by their length
- [x] [wav-files-**stats**](https://github.com/RustedBytes/wav-files-stats): Calculate statistics of a folder with WAV files
- [x] [wav-files-**trim**](https://github.com/RustedBytes/wav-files-trim): Automatically detect and trim silence from the start/end of WAV files, with optional threshold settings
- [x] [wav-files-**denoise**](https://github.com/RustedBytes/wav-files-denoise): Apply noise reduction tool [*nnnoiseless*](https://github.com/jneem/nnnoiseless) to remove background noise from WAV files
- [x] [wav-files-**denoise-api**](https://github.com/RustedBytes/wav-files-denoise-api): Apply noise reduction API to remove background noise from WAV files
- [ ] [wav-files-**vad-api**](https://github.com/RustedBytes/wav-files-vad-api): Extract speech using an API that performs Voice Speech Detection for WAV files
- [ ] [wav-files-**tempo**](https://github.com/RustedBytes/wav-files-tempo): Adjust playback speed/tempo of WAV files without altering pitch (using time-stretching algorithms like WSOLA)
- [ ] [wav-files-**mix**](https://github.com/RustedBytes/wav-files-mix): Overlay or blend multiple WAV files into a single output, with volume balancing and channel mapping (e.g., stereo mixdown)
- [x] [wav-files-**echo**](https://github.com/RustedBytes/wav-files-echo): Add echo, reverb, or chorus effects to WAV files using delay-based DSP parameters (e.g., decay time, wet/dry mix)

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

</details>

## Authors

- Yehor Smoliakov (contact: <egorsmkv@gmail.com>)

## Cite

```
@software{Smoliakov_Wav_Files_Toolkit_2025,
  author = {Smoliakov, Yehor},
  month = oct,
  title = {{WAV Files Toolkit}},
  url = {https://github.com/RustedBytes/wav-files-toolkit},
  version = {0.2.0},
  year = {2025}
}
```
