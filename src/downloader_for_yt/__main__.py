from pathlib import Path

import cmd2
import yt_dlp

BASE_PATH = Path.cwd() / "videos"

url = "https://youtu.be/UYXULc8E5fs?si=SbLVl-91F3eULrmu"


def main():
    print(BASE_PATH)

    yt = yt_dlp.YoutubeDL(
        {"paths": {"home": str(BASE_PATH)}, "listformats": True}
    )
    yt.download(url)


# if __name__ == "__main__":
#     main()


class DownloaderApp(cmd2.Cmd):
    """CMD2 application for the video downloading"""

    def do_list_all_formats(self, line: cmd2.parsing.Statement):
        yt = yt_dlp.YoutubeDL({"listformats": True})

        yt.download(str(line))

    download_parser = cmd2.Cmd2ArgumentParser()
    download_parser.add_argument("url", type=str)
    download_parser.add_argument("-p", "--path", type=str)

    @cmd2.with_argparser(download_parser)
    def do_default_download(self, line: cmd2.parsing.Statement):
        path = line.path if line.path else str(BASE_PATH)

        yt = yt_dlp.YoutubeDL({"paths": {"home": path}})

        yt.download(str(line.url))

    download_parser_with_format = cmd2.Cmd2ArgumentParser()
    download_parser_with_format.add_argument("url", type=str)
    download_parser_with_format.add_argument("-p", "--path", type=str)
    download_parser_with_format.add_argument(
        "-f",
        "--format",
        type=str,
        help="Format for the download. It should be like <video-format-code>+<audio-format-code>",
    )

    @cmd2.with_argparser(download_parser_with_format)
    def do_download_with_format(self, line: cmd2.parsing.Statement):
        path = line.path if line.path else str(BASE_PATH)

        yt = yt_dlp.YoutubeDL(
            {"paths": {"home": path}, "format": str(line.format)}
        )

        yt.download(str(line.url))


if __name__ == "__main__":
    import sys

    c = DownloaderApp()
    sys.exit(c.cmdloop())
