import pathlib
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
file_type_variation_list = ['.exe', '.ini', '.zip', '.msi', '.iso', '.torrent']
for file in downloads_path.iterdir():
    if file.is_file():
        extension = file.suffix
        if extension not in file_type_variation_list:
            file_type_variation_list.append(extension)
        if extension == '.exe':
            shutil.move(file, programs_path)

print(file_type_variation_list)
