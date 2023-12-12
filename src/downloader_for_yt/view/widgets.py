from enum import Enum

import PySimpleGUI as sg
from .widgets_keys import WidgetKeys

BACKGROUND_COLOR = "#44aaca"
INITIAL_FOLDER = "C:/Users/Usuario/Desktop"
ERROR_MESSAGE = "Please, enter a valid URL"
HEADER_MESSAGE = "Paste the YouTube video/ playlist link and click the button"

FORMAT_SELECTOR_OPTIONS = ["MP4", "Webm"]

LIST_HEIGHT = 10
LIST_WIDTH = 10


class ButtonTexts(Enum):
    SUBMIT = "Submit"
    LOAD_VIDEO = "Load video"


fbDownloadDirectory: sg.FolderBrowse = sg.FolderBrowse(key=str(WidgetKeys.browser), tooltip="Folder which will store "
                                                                                            "all the videos",
                                                       target="folder_text", initial_folder=INITIAL_FOLDER)
"""
Folder picker
"""

# region Buttons
btSubmit: sg.Button = sg.Button(button_text=ButtonTexts.SUBMIT.value, key=WidgetKeys.submit.value)
"""
Button pressed to start download
"""

btLoad: sg.Button = sg.Button(button_text=ButtonTexts.LOAD_VIDEO.value, key=WidgetKeys.load_video.value)
"""
Button pressed to load video properties
"""
# endregion

# region Listboxes
lbVideoFormat: sg.Listbox = sg.Listbox(values=[], key=WidgetKeys.video_format.value,
                                       size=(LIST_WIDTH, LIST_HEIGHT),
                                       expand_x=True, horizontal_scroll=True)
"""
List showing format of video
"""

lbAudioFormat: sg.Listbox = sg.Listbox(values=[], key=WidgetKeys.audio_format.value,
                                       size=(LIST_WIDTH, LIST_HEIGHT),
                                       expand_x=True, horizontal_scroll=True)
"""
List showing format of video
"""

lbMixedFormat: sg.Listbox = sg.Listbox(values=[], key=WidgetKeys.mixed_format.value,
                                       size=(LIST_WIDTH, LIST_HEIGHT),
                                       expand_x=True, horizontal_scroll=True)
"""
List showing format of video and audio mixed (no FFMpeg needed)
"""
# endregion

show_format_list_checkbox: sg.Checkbox = sg.Checkbox(text="Show Format List", key=WidgetKeys.show_format.value)
"""
WIP: I don't really know what is this
"""


itURL = sg.InputText(tooltip="Video/ Playlist url", size=(50, 1), key=WidgetKeys.url.value)
"""
Input text that contains the selected video url
"""

cbDownloadExtension = sg.Combo(FORMAT_SELECTOR_OPTIONS, size=10, key="format_choose", default_value="MP3")
