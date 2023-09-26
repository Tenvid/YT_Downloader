import os
import PySimpleGUI as sg
import youtube_downloader

BACKGROUND_COLOR = "#44aaca"
INITIAL_FOLDER = "C:/Users/Usuario/Desktop"
ERROR_MESSAGE = "Please, enter a valid URL"
HEADER_MESSAGE = "Paste the YouTube video/ playlist link and click the button"


def main():
    layout = [
        [sg.Text(text=HEADER_MESSAGE, background_color=BACKGROUND_COLOR, key="header"), sg.Combo(['MP4', "MP3"], size=10, key="format_choose", default_value="MP3")],
        [sg.T("Root folder", background_color=BACKGROUND_COLOR),
         sg.FolderBrowse(key="browser", tooltip="Folder which will store all the videos",
                         target="folder_text", initial_folder=INITIAL_FOLDER),
         sg.Text(key="folder_text", text=INITIAL_FOLDER, background_color=BACKGROUND_COLOR)],
        [sg.T("FolderName", background_color=BACKGROUND_COLOR),
         sg.InputText(tooltip="Video folder name", key="name_input", size=(50, 1))],
        [sg.Button("Submit"), sg.InputText(tooltip="Video/ Playlist url", size=(50, 1), key="url")],
    ]
    sg.theme_background_color(BACKGROUND_COLOR)
    # Create the window
    window = sg.Window("YouTube Downloader", layout)
    # Create an event loop

    youtube_download(window)


def youtube_download(window):
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break

        # When "Submit" is pressed
        if event == "Submit":
            # Apply default values and check if url is valid
            if validate_values(values):
                link = values['url']
                root_folder = values['browser']
                video_folder_name = values['name_input']
                download_format = values["format_choose"]

                try:
                    command = f"python youtube_downloader.py \"{link}\" \"{root_folder}\" \"{video_folder_name}\" {download_format}"
                    print(command)
                    # Download videos
                    os.system(command)
                    # Show a correct popup
                    sg.popup_ok("Download has finished", background_color="green")
                except Exception as e:
                    sg.popup_error("An error occurred", e.args, background_color="#8e2536", button_color="#111133")
                    raise e
                pass


def validate_values(dict_values) -> bool:
    if dict_values['url'] == '':
        sg.popup_error("You have to enter a valid URL", title="Invalid URL", background_color="#8e2536", button_color="#111133", auto_close=False)
        return False
    if dict_values['browser'] == '' or not os.path.isdir(dict_values['browser']):
        dict_values['browser'] = INITIAL_FOLDER
    if dict_values['name_input'] == '':
        dict_values['name_input'] = "DefaultName"
    else:
        pass
        # dict_values['name_input'] = youtube_downloader.validate_title(dict_values['name_input'])
    return True


if __name__ == "__main__":
    main()
