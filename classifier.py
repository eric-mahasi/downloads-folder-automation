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


def move_file(dest_path):
    if os.path.isdir(dest_path):
        shutil.move(file, dest_path)
    else:
        os.mkdir(dest_path)
        shutil.move(file, dest_path)
        
        
for file in downloads_path.iterdir():
    if file.is_file():
        extension = file.suffix
        if extension in program_types:
            move_file(programs_path)
        elif extension in compressed_types:
            move_file(compressed_path)
        elif extension in doc_types:
            move_file(documents_path)
        elif extension in music_types:
            move_file(music_path)
        elif extension in video_types:
            move_file(video_path)
        elif extension in picture_types:
            move_file(pictures_path)
        else:
            move_file(other_path)
