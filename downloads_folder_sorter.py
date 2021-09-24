"""Downloads folder sorter

This script iterates through the files in a user's downloads folder on Windows and places each file in its appropriate
folder.

This file contains the following functions:

    * move_file - checks if the destination folder exists, creates it if it doesn't, then moves a file into it
    * sort_folder - iterates through the files in the folder
"""

import os.path
import shutil
import configparser
from pathlib import Path
""" Adds Config file for custom extention control """
config = configparser.ConfigParser()
config.read('config.ini')

pro_type = config['CONFIG']['PROGRAMS']
comp_type = config['CONFIG']['COMPRESSED']
doc_type = config['CONFIG']['DOCUMENTS']
mus_type = config['CONFIG']['MUSIC']
vid_type = config['CONFIG']['VIDEO']
pic_type = config['CONFIG']['PICTURES']

user = os.getenv('USERNAME')
downloads_path = Path("/Users/{}/Downloads".format(user))
programs_path = Path("/Users/{}/Downloads/Programs".format(user))
compressed_path = Path("/Users/{}/Downloads/Compressed".format(user))
documents_path = Path("/Users/{}/Downloads/Documents".format(user))
music_path = Path("/Users/{}/Downloads/Music".format(user))
video_path = Path("/Users/{}/Downloads/Video".format(user))
pictures_path = Path("/Users/{}/Downloads/Pictures".format(user))
other_path = Path("/Users/{}/Downloads/Other".format(user))

program_types = eval(pro_type)
compressed_types = eval(comp_type)
doc_types = eval(doc_type)
music_types = eval(mus_type)
video_types = eval(vid_type)
picture_types = eval(pic_type)


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
