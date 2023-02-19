from pathlib import Path

import requests
from canvasapi.file import File


class Request:
    def download_files(folder_directory: Path, file: File):
        file_path = Path(folder_directory, file.filename)
        if Path.is_file(file_path):
            print("File exist: ", file_path)
            return
        print("downloading file: ", file_path)
        response = requests.get(url=file.url)
        open(file_path, "wb").write(response.content)
