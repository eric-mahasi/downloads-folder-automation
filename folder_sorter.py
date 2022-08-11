"""Downloads folder sorter
This script iterates through the files in a user's folder on Windows and places each file in its appropriate
folder.
This file contains the following functions:
    * move_file - checks if the destination folder exists, creates it if it doesn't, then moves a file into it
    * sort_folder - iterates through the files in the folder
"""

import os
import json
import shutil
from pathlib import Path
from tkinter import Tk, Button, filedialog, messagebox, Grid


def move_file(file, destination):
    """Checks if the destination folder exists, creates it if it doesn't, then moves a file into it
    Parameters
    ----------
    file : Path
        the path to a file
    destination : Path
        the path to the destination folder
    """
    try:
        if not destination.exists():
            destination.mkdir(parents=True, exist_ok=True)
        shutil.move(file, destination)

    except shutil.Error as e:
        print(e)


def sort_folder_by_categories():
    """Iterates through the files in the folder, sorting them into sub-folders by extension."""
    folder_path = select_folder()
    with open("config.json", encoding="utf-8") as f:
        categories = json.load(f)

    extensions_map = {}
    for category in categories:
        folder_name = category["name"]
        for extension in category["extensions"]:
            extensions_map[extension] = folder_name

    for file in folder_path.iterdir():
        if file.is_file() and not file.name.startswith("."):
            destination = extensions_map.get(file.suffix, "Other")
            move_file(file, file.parent.joinpath(destination))
    messagebox.showinfo("File Sort", "All files were sorted")


def sort_folder_by_extensions():
    folder_path = select_folder()
    list_ = os.listdir(folder_path)
    for file_ in list_:
        _, ext = os.path.splitext(file_)
        ext = ext[1:]
        if ext == "":
            continue
        if not os.path.exists(f"{folder_path}/{ext}"):
            os.makedirs(f"{folder_path}/{ext}")
        shutil.move(f"{folder_path}/{file_}", f"{folder_path}/{ext}/{file_}")
    messagebox.showinfo("File Sort", "All files were sorted")


def select_folder():
    """Opens a file dialog to select a folder."""
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    return Path(filedialog.askdirectory())


def user_interface():
    root = Tk()
    root.title("Folder Sorter")
    root.geometry("250x150")

    x = (root.winfo_screenwidth() / 2) - (root.winfo_reqwidth() / 2)
    y = (root.winfo_screenheight() / 2) - (root.winfo_reqheight() / 2)
    root.geometry("+%d+%d" % (x, y))

    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    b1 = Button(root, text="Sort by Categories", command=sort_folder_by_categories)
    b2 = Button(root, text="Sort by Extensions", command=sort_folder_by_extensions)
    bl = [b1, b2]
    for row_no, _ in enumerate(bl):
        Grid.rowconfigure(root, row_no, weight=1)
    b1.grid(row=0, column=0, sticky="nsew")
    b2.grid(row=1, column=0, stick="nsew")

    root.mainloop()


if __name__ == "__main__":
    user_interface()
