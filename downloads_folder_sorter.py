"""Downloads folder sorter

This script iterates through the files in a user's downloads folder on Windows and places each file in its appropriate
folder.

This file contains the following functions:

    * move_file - checks if the destination folder exists, creates it if it doesn't, then moves a file into it
    * sort_folder - iterates through the files in the folder
"""

import os.path
import shutil
from pathlib import Path
import json

user = os.getenv('USERNAME')
downloads_path = Path("/Users/{}/Downloads".format(user))

with open('config.json', encoding='utf-8') as f:
    CATEGORIES = json.load(f)


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
            for category in CATEGORIES:
                if file.suffix in category['extensions']:
                    destination = file.parent.joinpath(category['name'])
                    move_file(file, destination)


if __name__ == '__main__':
    sort_folder()
