import logging
import re

import yt_dlp
import os


def main(link: str = None, root_folder: str = None, video_folder_name: str = None, video_format: str = None):
    logging.info(msg=f"Title: {root_folder}\n")
    logging.info(msg=f"Link: {link}\n")
    logging.info(msg=f"Video folder name: {video_folder_name}\n")
    logging.info(msg=f"Chosen format: {video_format}\n")

    try:
        try_download(link=link, root_videos=root_folder, video_folder_name=video_folder_name)
    except:
        # try:
        #     yt = pytube.Playlist(link)
        #     my_path = os.getcwd()
        #
        #     # Makes the title of the playlist not to contain invalid caracters for a path
        #     list_title = validate_title(yt.title)
        #
        #     # Get path of the folder which will contain the playlist
        #     folder = os.path.abspath(os.path.join(my_path, f"{root_folder}\\{video_folder_name}"))
        #     # Creates the folder if it doesn't exist
        #     try:
        #         os.mkdir(folder)
        #     except:
        #         print(f"Folder {folder} already exists so it won't be created")
        #         pass
        #
        #     # Downloads all the videos of the playlist
        #     for video in yt:
        #         try_download(link=video, video_folder_name=list_title, root_videos=folder, format=video_format)
        # except Exception as e:
        #     print(e.args)
        #     raise e
        print("error")
        pass
    else:
        print("Videos downloaded")


def set_elements(link, parser, root_folder, video_folder_name, video_format):
    _link = link or parser.link
    _root_folder = root_folder or parser.root_folder
    _video_folder_name = video_folder_name or parser.video_folder_name
    _video_format = video_format or parser.format
    return _link, _root_folder, _video_folder_name, _video_format


def show_format_list(link: str):
    if not link or not is_valid_link(link):
        return False


def is_valid_link(link: str):
    pattern = "^https:\/\/[0-9A-z.]+.[0-9A-z.]+.[a-z]+$"
    return re.match(pattern, link)


def try_download(link: str, video_folder_name, root_videos) -> None:
    out_path = os.path.join(root_videos, video_folder_name) + "/%(title)s.%(ext)s"

    dl_opts = {
        'outtmpl': out_path
    }

    yt = yt_dlp.YoutubeDL(dl_opts)

    info_dict = yt.extract_info(url=link)

    print(f"INFO DICT: {info_dict}")
    formats_table = yt.render_formats_table(info_dict)
    print(yt_dlp.options.get_executable_path())

    # yt.download([url])

    # try:
    #     yt = YouTube(url=link.replace('"', ''))
    #     print(yt.title)
    #     # Name of the folder which will contain the video
    #     video_folder = validate_title(video_folder_name)
    #
    #     # Path to the download folder
    #     download_folder = os.path.join(root_videos, video_folder)
    #
    #     logging.info(f"Folder path: {download_folder}")
    #
    #     print(download_folder)
    #     video = yt.streams
    #     print(video)
    #     video = video.filter(progressive=True)
    #
    #     print(video)
    #     video = video.order_by("resolution")
    #     print(video)
    #     video = video.last()
    #     print(video)
    #     # video = yt.streams.get_highest_resolution()
    #     print("A")
    #     video.download(download_folder)
    # except Exception as e:
    #     print(e)
    # Gets the best resolution and downloads the video in the specified path
    # if format == "MP3":
    #     print("mp3")
    #     audio = yt.streams.filter(only_audio=True).first()
    #     out_file = audio.download(download_folder)
    #     base, ext = os.path.splitext(out_file)
    #     new_file = base + ".mp3"
    #     os.rename(out_file, new_file)
    #     # download_audio(download_folder, yt)
    # elif format == "MP4":
    #     try:
    #         video = yt.streams.get_highest_resolution()
    #         print("video")
    #         video.download(download_folder)
    #     except Exception as e:
    #         print(e.args)
    #         raise e
    #     # download_video(download_folder, yt)
    # else:
    #     print("error format")
    #     raise Exception(f"Chosen format ({format}) isn't valid")


def download_video(download_folder, yt):
    video = yt.streams.get_highest_resolution()
    video.download(download_folder)


def download_audio(download_folder, yt):
    audio = yt.streams.filter(only_audio=True).first()
    out_file = audio.download(download_folder)
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)


def validate_title(old_title):
    title = old_title
    title = title.replace("{", "[")
    title = title.replace("}", "]")
    title = title.replace("\\", "_")
    title = title.replace("/", "_")
    title = title.replace("|", "_")
    title = title.replace(" ", "_")

    return title


if __name__ == "__main__":
    main()
