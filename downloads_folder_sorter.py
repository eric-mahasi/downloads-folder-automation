"""Downloads folder sorter

This script iterates through the files in a user's downloads folder on Windows and places each file in its appropriate
folder.

This file contains the following functions:

    * move_file - checks if the destination folder exists, creates it if it doesn't, then moves a file into it
    * sort_folder - iterates through the files in the folder
"""
import os
import os.path
import shutil
import pathlib
import json

with open('categories.json', encoding='UTF-8') as f:
    CATEGORIES = json.load(f)


def main():
    username = os.getenv('USERNAME')
    downloads_folder = pathlib.Path(f'/Users/{username}/Downloads')
    sort_folder(downloads_folder)


def sort_folder(folder: pathlib.Path):
    """Iterates through the files in the folder"""
    for file in folder.iterdir():
        sort_file(file)


def sort_file(file: pathlib.Path):
    """moves an individual file into the correct folder"""
    if file.is_file():
        for category in CATEGORIES:
            if file.suffix in category['extensions']:
                destination = file.parent.joinpath(category['name'])
                move_file(source=file, destination=destination)


def move_file(source: str, destination: str):
    """Checks if the destination folder exists, 
    creates it if it doesn't, 
    then moves a file into it
    Parameters
    ----------
    file : Path
        the path to a file
    dest_path : Path
        the path to the destination folder
    """
    if os.path.isdir(destination):
        shutil.move(source, destination)
    else:
        os.mkdir(destination)
        shutil.move(source, destination)


if __name__ == '__main__':
    main()
