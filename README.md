# Simple Voice Extract

## Purpose
This script utilizes Whisper to extract only the portions of the audio where sentences are present. The resulting audio will contain only voices, which can be used for training other voice models or for quick editing of podcasts or YouTube videos.

## Instructions

1. Install Whisper and its dependencies:

   ```bash
   pip install git+https://github.com/openai/whisper.git
   pip install setuptools-rust
   ```

2. Install FFmpeg:

   - Visit [ffmpeg home](https://ffmpeg.org/) and follow the installation instructions for your operating system.

   OR

   - For Windows users, you can directly download FFmpeg using [this link](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip).

3. Add FFmpeg's binary folder to the environment PATH (folder containing ffmpeg.exe).

4. Run the script to extract the voices from the audio:

   ```bash
   python your_script.py
   ```
