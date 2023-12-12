from downloader_for_yt.model.VideoFormat import VideoFormat
from downloader_for_yt.view.widgets import lbVideoFormat, lbAudioFormat, lbMixedFormat


def _fill_video_list(format_list: list[VideoFormat]):
    video_list = []
    for video_format in format_list:
        if video_format.has_video() and not video_format.has_audio():
            video_list.append(video_format)
    lbVideoFormat.update(values=video_list)


def _fill_audio_list(format_list: list[VideoFormat]):
    audio_list = []
    for video_format in format_list:
        if not video_format.has_video() and video_format.has_audio():
            audio_list.append(video_format)
    lbAudioFormat.update(values=audio_list)


def _fill_mixed_list(format_list: list):
    mixed_list = []
    for video_format in format_list:
        if video_format.has_video() == video_format.has_audio():
            mixed_list.append(video_format)
    lbMixedFormat.update(values=mixed_list)


def fill_lists(format_list: list):
    _fill_video_list(format_list)
    _fill_audio_list(format_list)
    _fill_mixed_list(format_list)