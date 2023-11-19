#! /usr/bin/env python

import os
import time

from dotenv import load_dotenv
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from watchdog.observers import Observer

from file_utilities import *


class Handler(FileSystemEventHandler):
    """Class that monitor that target folder.

    Args:
        FileSystemEventHandler (Class): Class Base file system event handler.
        link: https://python-watchdog.readthedocs.io/en/stable/api.html#module-watchdog.events

    """

    # That you can override files or add extension and verify function in file_utilities.py.
    FILE_TYPE_FOLDERS = {
        "code": is_code_file,
        "text": is_text_file,
        "pdf": is_pdf_file,
        "audio": is_mp3_file,
        "images": is_image_file,
        "x86_64_bundle": is_file_bundle,
        "videos": is_video_file,
        "word-documents": is_doc_file,
        "spreadsheets": is_spreadsheet_file,
        "presentation-files": is_presentation_file,
        "executable-files": is_executable_file,
    }

    @staticmethod
    def on_created(event):
        pass

    @staticmethod
    def on_modified(event):
        """Method that monitor an event modified

        Args:
            event (_type_): args that representing event in source folder.
        """
        if os.path.isdir(event.src_path):
            return

        for folder_name, check_function in Handler.FILE_TYPE_FOLDERS.items():
            if check_function(event):
                path_to_folder = make_folder(folder_name)
                move_to_new_corresponding_folder(event, path_to_folder)
                return

    @staticmethod
    def on_deleted(event):
        pass

    @staticmethod
    def on_moved(event):
        pass


if __name__ == "__main__":
    load_dotenv()

    file_change_handler = Handler()

    # Observer thread that schedules watching directories and dispatches calls to event handlers.
    # API Reference: https://python-watchdog.readthedocs.io/en/stable/api.html#watchdog.observers.Observer
    observer = Observer()

    # Get target folder utilizing python-dotenv and change directory specified in .env
    os.chdir(os.getenv("DIRECTORY_OF_CLEANER"))
    observer.schedule(
        file_change_handler,
        os.getcwd(),
        recursive=False,
    )
    # Start thread.
    observer.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
