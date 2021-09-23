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

program_types = ('.exe', '.pkg', '.dmg')
compressed_types = ('.zip', '.rar')
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
music_types = ('.mp3', '.wav')
video_types = ('.mp4', '.gif',)
picture_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
for file in downloads_path.iterdir():
    if file.is_file():
        extension = file.suffix
        if extension == '.exe':
            shutil.move(file, programs_path)

