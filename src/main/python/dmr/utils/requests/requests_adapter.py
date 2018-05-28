from pathlib import Path

import requests
import click

CHUNK_SIZE = 1024


class RequestsAdapter(object):

    def __init__(self, color: str):
        self.color = color

    def download_file_to_directory(self, download_url: str, full_download_path: Path):
        response = requests.get(download_url, stream=True)
        size = int(response.headers.get("content-length"))
        with click.open_file(full_download_path, "wb") as f:
            content_iter = response.iter_content(chunk_size=CHUNK_SIZE)
            with click.progressbar(content_iter, length=size / 1024, color=True,
                                   fill_char=click.style('#', fg=self.color)) as bar:
                for chunk in bar:
                    if chunk:
                        f.write(chunk)
                        f.flush()
