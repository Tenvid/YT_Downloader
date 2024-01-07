import argparse
import logging
import os

import PySimpleGUI as sg
import yt_dlp

from downloader_for_yt.model import list_manager
from downloader_for_yt.model.VideoFormat import VideoFormat
from downloader_for_yt.view.rows import (
    folder_row,
    format_lists_row,
    header_row,
    input_row,
    list_headers_row,
    submit_row,
)
from downloader_for_yt.view.widgets import (
    INITIAL_FOLDER,
    itURL,
    lbAudioFormat,
    lbVideoFormat,
)
from downloader_for_yt.view.widgets_keys import WidgetKeys


def get_arguments():
    args = argparse.ArgumentParser(
        prog="Universal Downloader",
        description="This app downloads web videos",
    )

    args.add_argument('link', type=str)
    args.add_argument('root_folder', type=str, default="C:/Users/Usuario/Desktop")
    args.add_argument('video_folder_name', type=str)
    args.add_argument('format', type=str, choices=["MP3", "MP4"])
    return args.parse_args()


def config_log():
    logging.basicConfig(filename="log.txt",
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)


def generate_layout():
    return [
        header_row,
        folder_row,
        list_headers_row,
        format_lists_row,
        input_row,
        submit_row
    ]


def popup_invalid_url_error(url) -> bool:
    """
    Shows an error screen in case url is empty
    :param url: Video url
    :return: If there is an error
    """
    if url == '':
        sg.popup_error("You have to enter a valid URL", title="Invalid URL", background_color="#8e2536",
                       button_color="#111133", auto_close=False)
        return True
    return False


def download_video_audio(video_code: str, audio_code: str):
    dl_options = {
        'outtmpl': './videos/%(uploader)s/%(title)s.%(ext)s',
        'format': f'{video_code}+{audio_code}',
    }

    yt = yt_dlp.YoutubeDL(dl_options)

    yt.download(itURL.get())


def process_event(event: str):
    """
    When an event is received, executes an action depending on it
    :param event: Event key
    """
    if not event:
        return

    if event == WidgetKeys.submit.value:
        # TODO: Check if a video has been already loaded
        print("Submitted")
        print(f"Selected video: {lbVideoFormat.get()[0]}")
        print(f"Selected audio: {lbAudioFormat.get()[0]}")

        selected_video: VideoFormat = lbVideoFormat.get()[0]
        selected_audio: VideoFormat = lbAudioFormat.get()[0]

        download_video_audio(selected_video.get_id(), selected_audio.get_id())

    elif event == WidgetKeys.load_video.value:
        try:
            video_info = _get_video_info()
            processed_formats_list = get_processed_formats_list(video_info)
            list_manager.fill_lists(processed_formats_list)

        except yt_dlp.utils.DownloadError:
            popup_invalid_url_error(itURL.get())


def _get_video_info():
    with yt_dlp.YoutubeDL() as yt:
        video_info = yt.extract_info(itURL.get(), download=False)
    return video_info


def get_processed_formats_list(video_info):
    """
    By passing a dict with the info of a video, returns a list of :class:`VideoFormat`
    :param video_info: Dict which contains info about a video
    :return: list of available :class:`VideoFormat`
    """
    extracted_video_formats = video_info["formats"]
    processed_formats_list = _get_format_list(extracted_video_formats)
    return processed_formats_list


def _get_format_list(extracted_formats: dict):
    """
    Given the dict element of the formats, returns a list of :class:`VideoFormat`
    :param extracted_formats: Dict element that contains a format of yt_dlp
    :return: list of :class:`VideoFormat`
    """
    processed_formats = []
    for f in extracted_formats:
        # TODO: Remove hardcoded strings in dictionaries
        insert = VideoFormat(f['format_id'],
                             f.get('resolution', 'N/A'),
                             f.get('vcodec') != 'none',
                             f.get('acodec') != 'none',
                             f['ext'],
                             f["vbr"])
        processed_formats.append(insert)
    return processed_formats


def validate_values(dict_values) -> bool:
    if popup_invalid_url_error(dict_values['url']):
        return False

    if dict_values['browser'] == '' or not os.path.isdir(dict_values['browser']):
        dict_values['browser'] = INITIAL_FOLDER
    if dict_values['name_input'] == '':
        dict_values['name_input'] = "DefaultName"
    else:
        pass
        # dict_values['name_input'] = youtube_downloader.validate_title(dict_values['name_input'])
    return True


def render_window(window):
    """
    Starts the program. Reads the values

    :param window: Window that will be rendered
    """

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break

        process_event(event)


def main():
    """
    Main function of program
    """
    layout = generate_layout()

    window = sg.Window("Universal Downloader", layout, size=(1280, 720))

    render_window(window)


if __name__ == "__main__":
    main()
