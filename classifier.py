import pathlib
from pathlib import Path

downloads_folder_path = Path("/Users/ericm/Downloads")
contents = pathlib.Path(downloads_folder_path).iterdir()
for path in contents:
    print(path)
