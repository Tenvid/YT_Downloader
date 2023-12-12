import PySimpleGUI as sg
import downloader_for_yt.view.widgets as widgets

header_row = [sg.Text(text=widgets.HEADER_MESSAGE, background_color=widgets.BACKGROUND_COLOR, key="header"),
              sg.Combo(widgets.FORMAT_SELECTOR_OPTIONS, size=10, key="format_choose", default_value="MP3")]
"""
Contains labels explaining how the program works
"""

folder_row = [sg.T("Root Folder:", background_color=widgets.BACKGROUND_COLOR), widgets.fbDownloadDirectory,
              sg.Text(key="folder_text", text=widgets.INITIAL_FOLDER, background_color=widgets.BACKGROUND_COLOR)]
"""
Contains the folder browser
"""

list_headers_row = [sg.T("Only Video", expand_x=True), sg.T("OnlyAudio", expand_x=True), sg.T("All", expand_x=True)]
"""
Contains the headers for the formats lists
"""

format_lists_row = [widgets.lbVideoFormat, widgets.lbAudioFormat, widgets.lbMixedFormat]
"""
Contains the lists of formats for video and audio
"""

input_row = [widgets.btSubmit,
             widgets.itURL]
"""
Contains the input text for the url
"""

submit_row = [widgets.btLoad, widgets.show_format_list_checkbox]
"""
Contains the button which generates the lists
"""