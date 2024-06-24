import re
import sys
from argparse import Namespace
from pathlib import Path

import cmd2
import yt_dlp

BASE_PATH = Path.cwd() / "videos"


class DownloaderApp(cmd2.Cmd):
    """CMD2 application for the video downloading"""

    def validate_url(self, url: str) -> bool:
        """Check if the url is valid.

        Args:
            url (str): Url to be checked

        Returns:
            bool: If url is valid
        """

        return re.match("(https:\/\/youtu\.be\/)([a-zA-Z0-9?=\-_]*)", url)

    def do_list_all_formats(self, line: Namespace):
        """Shows all the available formats for the given url.

        Args:
            line (Namespace): Line arguments
        """

        yt = yt_dlp.YoutubeDL({"listformats": True})

        yt.download(str(line))

    download_parser = cmd2.Cmd2ArgumentParser()
    download_parser.add_argument(
        "url", type=str, help="Url which will be downloaded."
    )
    download_parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Path of the folder where the video will be downloaded. Can be absolute or relative.",
    )

    @cmd2.with_argparser(download_parser)
    def do_default_download(self, line: Namespace):
        """Download given video url. A path can be specified.

        Args:
            line (Namespace): Line arguments
        """

        if not self.validate_url(line.url):
            return

        path = line.path if line.path else str(BASE_PATH)

        yt = yt_dlp.YoutubeDL({"paths": {"home": path}})

        yt.download(str(line.url))

    download_parser_with_format = cmd2.Cmd2ArgumentParser()
    download_parser_with_format.add_argument(
        "url", type=str, help="Url which will be downloaded."
    )
    download_parser_with_format.add_argument(
        "-p",
        "--path",
        type=str,
        help="Path of the folder where the video will be downloaded. Can be absolute or relative.",
    )
    download_parser_with_format.add_argument(
        "-f",
        "--format",
        type=str,
        help="Format for the download. It should be like <video-format-code>+<audio-format-code>.",
    )

    @cmd2.with_argparser(download_parser_with_format)
    def do_download_with_format(self, line: Namespace):
        """Download video with specified format. A path can be specified.

        Args:
            line (Namespace): Line arguments
        """

        path = line.path if line.path else str(BASE_PATH)

        yt = yt_dlp.YoutubeDL(
            {"paths": {"home": path}, "format": str(line.format)}
        )

        yt.download(str(line.url))


if __name__ == "__main__":
    app = DownloaderApp()
    sys.exit(app.cmdloop())
