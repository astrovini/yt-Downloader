# YouTube Playlist Downloader

A command-line tool to download all videos from a YouTube playlist as high-quality MP3 files into a user-specified folder.

## Features
- Downloads every video in a playlist as MP3
- High-quality audio conversion using ffmpeg
- Simple command-line interface

## Requirements
- Python 3.7+
- yt-dlp
- ffmpeg (must be installed and available in PATH)

## Usage
Run the script and follow the prompts:
```
python playlist_downloader.py
```

You will be asked to:
1. Enter the YouTube playlist URL.
2. Enter a name for the playlist folder. All songs will be saved as MP3s in a folder with this name inside your Downloads directory.

Example session:
```
$ python playlist_downloader.py
Enter the YouTube playlist URL: https://www.youtube.com/playlist?list=PL123...
Enter a name for the playlist folder (will be created in Downloads): MyMusicFolder
Downloading to: /home/youruser/Downloads/MyMusicFolder
```

## How it works
- The script prompts you for a YouTube playlist link and a folder name.
- It creates a folder with your chosen name inside your Downloads directory (~/Downloads/YourFolderName).
- It uses yt-dlp to download each video in the playlist and ffmpeg to convert the audio to high-quality MP3 files.
- All MP3s are saved in the specified folder.

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Ensure ffmpeg is installed on your system:
   - **Linux:**
     ```
     sudo apt install ffmpeg
     ```
   - **macOS:**
     ```
     brew install ffmpeg
     ```
   - **Windows:**
     Download from [ffmpeg.org/download](https://ffmpeg.org/download.html), extract, and add the `bin` folder to your PATH.

---

## Coming soon
- **Graphical User Interface (GUI):** A user-friendly desktop app for easier playlist and song downloads.
- **Single Video/Song Download:** Download individual YouTube videos or songs as MP3s.
- **Spotify Integration:** Download and convert Spotify playlists and tracks (requires user-provided Spotify credentials).


## TODO:
- downloadable package and web page only version
- show and list which songs failed to download