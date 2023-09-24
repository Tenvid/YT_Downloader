import logging
import pytube
import os
import argparse


def get_arguments():
    args = argparse.ArgumentParser(
        prog="YouTube Downloader",
        description="This app downloads YT videos",
    )

    args.add_argument('link', type=str)
    args.add_argument('root_folder', type=str, default="C:/Users/Usuario/Desktop")
    args.add_argument('video_folder_name', type=str)
    return args.parse_args()


def config_log():
    logging.basicConfig(filename="log.txt",
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)


def main():
    config_log()
    parser = get_arguments()

    link = parser.link
    root_folder = parser.root_folder
    video_folder_name = parser.video_folder_name

    logging.info(msg=f"title: {root_folder}")
    logging.info(msg=f"link: {link}")
    logging.info(msg=f"video folder name: {video_folder_name}")

    try:
        download_video(link=link, root_videos=root_folder, video_folder_name=video_folder_name)
    except:
        try:
            yt = pytube.Playlist(link)
            my_path = os.getcwd()

            # Makes the title of the playlist not to contain invalid caracters for a path
            list_title = validate_title(yt.title)

            # Get path of the folder which will contain the playlist
            folder = os.path.abspath(os.path.join(my_path, f"{root_folder}\\{video_folder_name}"))
            # Creates the folder if it doesn't exist
            try:
                os.mkdir(folder)
            except:
                print(f"Folder {folder} already exists so it won't be created")
                pass

            # Downloads all the videos of the playlist
            for video in yt:
                download_video(link=video, video_folder_name=list_title, root_videos=folder)
        except Exception as e:
            print(e.args)
            raise e
    else:
        print("Videos downloaded")


def download_video(link: str, video_folder_name, root_videos) -> None:
    yt = pytube.YouTube(link)
    # Name of the folder which will contain the video
    video_folder = validate_title(video_folder_name)

    # Path to the download folder
    download_folder = os.path.join(root_videos, video_folder)

    logging.info(f"Folder path: {download_folder}")

    # Gets the best resolution and downloads the video in the specified path
    video = yt.streams.get_highest_resolution()
    video.download(download_folder)


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
