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

  Add this script to run in background in machine. In Linux it's necessary add script in systemd. If do not know systemd, this link [Systemd](https://e-tinet.com/systemd/) show little about it.
   

  **_Note_**:
  in this part, reading above link and know about systemd and dependecy to distribution of *_Linux_* path to systemd or version can be different. So search and confirm both information first.

  For distribution based in *_Debian_* or *_Ubuntu_* need add script in services of **systemd**. Create and edit this path in system **_/etc/systemd/system/_** in below an example in my system, refers in my computer please edit according to directory and computer. In this article explain well [article](https://embarcados.com.br/systemd-adicionando-scripts-na-inicializacao-do-linux/).


  * Create file with some edit text, in this case using *_nano_*. 
   ![Alt text](<images/systemd.png>)
    image create in path cited above with name **'cleaner_folder_download.service'** and add with poetry to run script, but your run script with python normally. Script have *_shebang_* to use with python of own machine or virtualenv


 * **Windows**

   In project exists pyinstaller to create executable. This, can be add in background also.

   * [Pyinstaller](https://pyinstaller.org/en/stable/)

   Run command terminal windows.
   ```
   pyinstaller --onefile --noconsole .\cleaner_folder_download.py
   ```
   in the folder, after run command above exists a folder *dist* create shortcut executable and move executable file to startup windows.
   type shell windows:
   ```
   shell:Startup
   ```
   add shortcut executable windows.Done script run background computer.


   

    


  
      
   













