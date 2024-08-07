import sys
from argparse import Namespace
from pathlib import Path
from typing import Dict

import cmd2
import ffmpeg
import yt_dlp
from yt_dlp.utils import DownloadError

BASE_PATH = Path.cwd() / "videos"


class DownloaderApp(cmd2.Cmd):
    """CMD2 application for the video downloading"""

    def __init__(self):
        super().__init__()
        del cmd2.Cmd.do_alias
        del cmd2.Cmd.do_edit
        del cmd2.Cmd.do_ipy
        del cmd2.Cmd.do_macro
        del cmd2.Cmd.do_py
        del cmd2.Cmd.do_run_pyscript
        del cmd2.Cmd.do_run_script
        del cmd2.Cmd.do_shell
        del cmd2.Cmd.do_shortcuts
        del cmd2.Cmd.do_set
        self.do_exit = self.do_quit

    def preloop(self):
        self.poutput(
            "Welcome to the YT Video Downloader. Here you have a list with the available commands"
        )
        self.do_help("-v")

    def do_list_all_formats(self, line: Namespace):
        """Shows all the available formats for the given url.

        Args:
            line (Namespace): Line arguments
        """

        yt = yt_dlp.YoutubeDL({"listformats": True})
        try:
            yt.download(str(line))
        except DownloadError:
            self.perror(
                "There was an error downloading data. Please check your internet connection and make sure url is correct."
            )

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
        """Download given video url with the best quality available. A path can be specified.

        Args:
            line (Namespace): Line arguments
        """

        path = line.path if line.path else str(BASE_PATH)

        yt = yt_dlp.YoutubeDL({"paths": {"home": path}})
        try:
            yt.download(str(line.url))
        except DownloadError:
            self.perror(
                "There was an error downloading the file. Please check your internet connection and make sure url is correct."
            )

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
        "-v",
        "--video_codec",
        type=int,
        help="Format id for the video. Leave empty for only download audio.",
    )
    download_parser_with_format.add_argument(
        "-a",
        "--audio_codec",
        type=int,
        help="Format id for the audio. Leave empty for only download video.",
    )

    @cmd2.with_argparser(download_parser_with_format)
    def do_download_with_format(self, line: Namespace):
        """Download video with specified format for video and audio. A path can be specified.

        Args:
            line (Namespace): Line arguments
        """

        if not line.video_codec and not line.audio_codec:
            self.perror(
                "You have to enter a video or audio format to download. Use list_formats to know them."
            )
            return

        path = line.path if line.path else str(BASE_PATH)

        yt = yt_dlp.YoutubeDL(
            {
                "paths": {"home": path},
                "format": str(f"{line.video_codec}+{line.audio_codec}"),
            }
        )

        try:
            yt.download(str(line.url))
        except DownloadError:
            self.perror(
                "There was an error downloading file. Please check your internet connection and make sure url is correct."
            )

    def _get_specified_format_by_id(
        self, info_dict: Dict, format_id: int
    ) -> Dict:
        for form in info_dict["formats"]:
            if form["format_id"] == str(format_id):
                return form
        return None

    video_reformatter_parser = cmd2.Cmd2ArgumentParser()
    video_reformatter_parser.add_argument(
        "-i",
        "--input",
        help="Path of the video you want to convert.",
        type=Path,
        required=True,
    )
    video_reformatter_parser.add_argument(
        "-e",
        "--extension",
        help="Extension that you want to give the reformatted video.",
        type=str,
        required=True,
    )
    video_reformatter_parser.add_argument(
        "-o",
        "--output",
        help="Folder which will contain reformatted video. Default value: './videos'",
        type=Path,
    )

    @cmd2.with_argparser(video_reformatter_parser)
    def do_reformat_video(self, line: Namespace):
        """Change extension of a video.

        Args:
            line (Namespace): _description_
        """

        input_video = Path(line.input)
        output_path = Path(line.output) if line.output else BASE_PATH
        video_title = str(line.input).replace("\\", "/").split("/")[-1]

        (
            ffmpeg.input(Path(input_video))
            .output(str(output_path / video_title) + "." + line.extension)
            .run()
        )


if __name__ == "__main__":
    app = DownloaderApp()
    sys.exit(app.cmdloop())
