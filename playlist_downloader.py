import sys
import os
import yt_dlp
import subprocess


def download_playlist(playlist_url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': False,
        'ignoreerrors': True,
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


def main():
    import getpass
    if sys.version_info >= (3, 0):
        input_func = input
    else:
        input_func = raw_input

    playlist_url = input_func("Enter the YouTube playlist URL: ").strip()
    default_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    folder_name = input_func("Enter a name for the playlist folder (will be created in Downloads): ").strip()
    if not folder_name:
        print("Folder name cannot be empty.")
        sys.exit(1)
    output_folder = os.path.join(default_downloads, folder_name)
    print(f"Downloading to: {output_folder}")
    download_playlist(playlist_url, output_folder)

if __name__ == "__main__":
    main()
