# YT_Downloader (Detailed)

This is the quickstart guide for people who aren't familiar with Windows CMD/ Linux Terminal or running python files.

## Steps

- Python installing
- Python-pip installing
- Downloading the files
- Reaching the files
- Getting ready to run the files
- Running the files
- Some tips

## Python installing

### Windows
Go to the official site and click the download button (you can choose between newer or older versions) to get "python-X.X.X-amd64.exe"
Now double-click the file and install python on your computer

### Linux
Open a terminal and run ``` sudo apt install python ```

## Python pip installing

### Windows & Linux
Go to the [official python guide](https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line) and follow the steps to install python-pip

## Downloading the files

In [this repository](https://github.com/Tenvid/YT_Downloader), click on code button and download it as a zip

## Reaching the files

### Windows & Linux

- Open the folder where the files have been downloaded in the file explorer and copy the adress.
- Open a CMD/Terminal and write ``` cd " ADDRESS_THAT_YOU_HAVE_COPIED " ``` (IMPORTANT: we have to write the quotes (""))
- Unzip the file
- Go to ``` ...\YT_Downloader-main\src\downloader_for_yt\ ```

In this folder there should be some files:
- init.py (irrelevant)
- ui.py (the script which will run the graphic interface of the app)
- youtube_downloader (script wich will execute the download)
- requierements.txt (python dependencies which we will install)

## Getting ready to run the files

### Windows & Linux

Without exiting the folder run ``` pip install -r requirements.txt ```

## Running the files
