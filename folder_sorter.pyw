"""Folder sorter
This script iterates through the files in a user's folder on Windows and places each file in its appropriate folder, it can sort by categories or by extensions. There's a config file that contains the categories.
    You can use it in two ways:
    1. Via the command line, here you specify the method and folder to be sorted.
        > python folder_sorter.pyw sort_c 
        > python folder_sorter.pyw sort_c "<path>"
        > python folder_sorter.pyw sort_e "<path>"
    2. Via the GUI,with both options and a popup with the target directory.
"""

import json
import os
import shutil
import sys
from pathlib import Path
from tkinter import Tk, Button, filedialog, messagebox, Grid


def set_global_variables():
    """
    Set global variables.
    """
    global SORT_METHOD
    global FOLDER_PATH
    SORT_METHOD = sys.argv[1] if len(sys.argv) > 1 else None
    FOLDER_PATH = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(get_download_path())


def user_interface():
    """
    User interface for the sorting app.

    Parameters
    ----------
    root : Tk
        The root window.

    Returns
    -------
    None

    Examples
    --------
    >>> user_interface()

    """
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


def show_message_box():
    messagebox.showinfo("Folder Sorter", "All files were sorted in their subfolders")


def select_folder():
    """
    Select a folder, if is not via GUI and has not specified a folder, Downloads is the default.

    Returns
    -------
    str
        The path of the selected folder.
    """
    if SORT_METHOD in ["sort_c", "sort_e"]:
        return FOLDER_PATH
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    return Path(filedialog.askdirectory())


def get_download_path():
    """
    Returns the default downloads path for windows.

    Parameters
    ----------
    None

    Returns
    -------
    str
        The path to the downloads folder.

    Examples
    --------
    >>> get_download_path()
    'C:\\Users\\User\\Downloads'

    """
    import winreg

    sub_key = "SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
    downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
        location = winreg.QueryValueEx(key, downloads_guid)[0]
    return location


def move_file(file, destination):
    """
    Move a file to a destination folder.

    Parameters
    ----------
    file : str
        The file to be moved.
    destination : str
        The destination folder.

    Returns
    -------
    None

    Examples
    --------
    >>> move_file('/home/user/file.txt', '/home/user/Documents')

    """
    try:
        if not destination.exists():
            destination.mkdir(parents=True, exist_ok=True)
        shutil.move(file, destination)

    except shutil.Error as e:
        print(e)


def sort_folder_by_categories():
    """
    Sort files in a folder by categories set in the config file.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Examples
    --------
    >>> sort_folder_by_categories()
    """
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
    if SORT_METHOD not in ["sort_c", "sort_e"]:
        show_message_box()


def sort_folder_by_extensions():
    """
    Sort files in a folder by their extensions.

    Parameters
    ----------
    folder_path : str
        The path of the folder to be sorted.

    Returns
    -------
    None

    Examples
    --------
    >>> sort_folder_by_extensions()
    Folder Sorter: All files were sorted in their subfolders
    """

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
    if SORT_METHOD not in ["sort_c", "sort_e"]:
        show_message_box()


if __name__ == "__main__":
    set_global_variables()

    if SORT_METHOD == "sort_c":
        sort_folder_by_categories()
    elif SORT_METHOD == "sort_e":
        sort_folder_by_extensions()
    else:
        user_interface()
