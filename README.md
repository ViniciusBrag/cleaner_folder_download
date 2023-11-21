# cleaner_folder_download
A simple **script** that organize folders and files as the own extension. Script can change the folder target and the way organize files how want. 
This video below a simple demonstration in target folder Donwloads.

[Screencast from 20-11-2023 08:24:57.webm](https://github.com/ViniciusBrag/cleaner_folder_download/assets/87455091/797f3e5d-5dab-4747-a47b-bed3ebfdd408)

# Installation
**_Notes:_** The project using *Poetry* as python dependency management and packaging, but also exists requirements.txt to installation as pip.

*Link* [Poetry](https://python-poetry.org/docs/) to installation and information about it.

 With **Poetry** installed use this command to initialize and install dependencies to use script.

```
poetry install
```

Or with environment active:

```
pip install -r requirements.txt
```

When you clone this project there will be a folder named contrib and project with this structure. In the folder **_Contrib_** contain a example of configuration.

![Alt text](<images/Screenshot from 2023-11-20 21-04-42.png>)

Run this command to configuration. **Note** change content in file env-sample to your target folder. After run this:
```
cp contrib/env-sample .env
```


Run script with: *_Poetry_* or Python of your machine.
* Active *_Poetry_*
```
poetry shell
```

* Poetry **actived**
```
poetry run python -u cleaner_folder_download.py
```
* Python
```
python -u cleaner_folder_download.py
```

## Extra configuration
* **Add others extension** in script **_cleaner_folder_download.py_** specify your extension and configuration add function in **_file_utilities.py_**.

   ![Alt text](<images/Screenshot from 2023-11-20 21-29-27.png>)


* **Option**

  Add this script to run in background in machine. In Linux it's necessary add script in systemd. But whats systemd?
  [Systemd](https://e-tinet.com/systemd/)
   

   













