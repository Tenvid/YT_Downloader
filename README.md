# YT_Downloader

With this repo you can download a YouTube video or playlist

## Set up

First you need to get the source code, you can download it directly from GitHub or using ```git clone``` in the command line.

Once you have the code downloaded you have to move to the folder where are the python scripts ```...\YT_Downloader\src\downloader_for_yt\``` and
install the requirements.
```
pip install -r requirements.txt
```

## Launching it

After installing the requirements you only have to run the "ui.py" script.

```
python ui.py
```


## How to use

Once the program is open you will see a little window with some buttons and text fields.

- The first button opens a folder browser where you will select which folder will contain the video (by default: C:/Users/Usuario/Desktop)
- The first text field is the name that you will give to the folder of the video (by default: DefaultName)
- The second field is where you have to place the url from YT (if it is empty, an error pop up will appear)
- The last button launches the "downloader.py" and downloads the video or playlist wherever you have chosen before
- In the upper right part you will see a box where you can choose between MP4 or MP3
