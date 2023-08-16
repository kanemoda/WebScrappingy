import os
import gdown
import sys

def print_tutorial():
    tutorial = "Usage: python script.py [LINK] [DOWNLOAD_PATH]\n\nDescription: This script downloads files from a Google Drive folder using gdown."
    print(tutorial)

def download_files(link, download_path):
    os.makedirs(download_path, exist_ok=True)

    file_list = gdown.download_folder(link, quiet=False, output=download_path , remaining_ok = True)

    for filename in file_list:
        print(f"Downloaded: {filename}")

def main():
    if len(sys.argv) == 1:
        print_tutorial()
    else:
        link = sys.argv[1]
        download_path = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()

        download_files(link, download_path)
        print("Download completed.")

if __name__ == "__main__":
    main()
