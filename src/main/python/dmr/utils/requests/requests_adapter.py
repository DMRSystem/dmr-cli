from pathlib import Path


class RequestsAdapter(object):

    def download_file_to_directory(self, download_url: str, download_directory: Path):
        print('Downloading file to directory!')