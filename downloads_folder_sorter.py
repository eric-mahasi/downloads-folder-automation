"""Downloads folder sorter

This script iterates through the files in my downloads folder and places each file in its appropriate folder.
This file contains the following functions:

    * move_file - checks if the destination folder exists, creates it if it doesn't, then moves a file into it
    * sort folder - iterates through the files in the folder
"""

import os.path
import shutil
from pathlib import Path

downloads_path = Path("/Users/ericm/Downloads")
programs_path = Path("/Users/ericm/Downloads/Programs")
compressed_path = Path("/Users/ericm/Downloads/Compressed")
documents_path = Path("/Users/ericm/Downloads/Documents")
music_path = Path("/Users/ericm/Downloads/Music")
video_path = Path("/Users/ericm/Downloads/Video")
pictures_path = Path("/Users/ericm/Downloads/Pictures")
other_path = Path("/Users/ericm/Downloads/Other")

program_types = ('.exe', '.pkg', '.dmg', '.msi')
compressed_types = ('.zip', '.rar')
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
music_types = ('.mp3', '.wav')
video_types = ('.mp4', '.mkv',)
picture_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')


def move_file(file, dest_path):
    """Checks if the destination folder exists, creates it if it doesn't, then moves a file into it
    Parameters
    ----------
    file : Path
        the path to a file
    dest_path : Path
        the path to the destination folder
    """
    if os.path.isdir(dest_path):
        shutil.move(file, dest_path)
    else:
        os.mkdir(dest_path)
        shutil.move(file, dest_path)


def sort_folder():
    """Iterates through the files in the folder"""
    for file in downloads_path.iterdir():
        if file.is_file():
            extension = file.suffix
            if extension in program_types:
                move_file(file, programs_path)
            elif extension in compressed_types:
                move_file(file, compressed_path)
            elif extension in doc_types:
                move_file(file, documents_path)
            elif extension in music_types:
                move_file(file, music_path)
            elif extension in video_types:
                move_file(file, video_path)
            elif extension in picture_types:
                move_file(file, pictures_path)
            else:
                move_file(file, other_path)


if __name__ == '__main__':
    sort_folder()
