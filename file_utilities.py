import os
import shutil
from time import sleep


def extension_type(event):
    """Method for verify the only extension

    Args:
        event (_type_): args that representing event in source folder.

    """
    try:
        # Verify after the '.' in the source path.
        return event.src_path[event.src_path.rindex(".") + 1 :]
    except ValueError:
        return


def is_file_bundle(event):
    return extension_type(event) == "x86_64.bundle"


def is_text_file(event):
    return extension_type(event) == "txt"


def is_pdf_file(event):
    return extension_type(event) == "pdf"


def is_mp3_file(event):
    return extension_type(event) in ("mp3", "wav")


def is_image_file(event):
    return extension_type(event) in ("png", "jpg", "bmp", "gif", "raw")


def is_video_file(event):
    return extension_type(event) in ("mov", "mp4", "avi", "flv")


def is_doc_file(event):
    return extension_type(event) in ("doc", "docx")


def is_spreadsheet_file(event):
    return extension_type(event) in ("xls", "xlsx")


def is_presentation_file(event):
    return extension_type(event) in ("ppt", "pptx")


def is_code_file(event):
    return extension_type(event) in ("py", "cs", "js", "php", "html", "sql", "css")


def is_executable_file(event):
    return extension_type(event) in ("exe", "msi", "deb", "sh")


def make_folder(foldername):
    os.chdir(os.getenv("DIRECTORY_OF_CLEANER"))
    if os.path.exists(foldername):
        print('Folder already exists, skipping creation')
        return os.getcwd() + os.sep + str(foldername)
    else:
        os.mkdir(str(foldername))
        return os.getcwd() + os.sep + str(foldername)


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
        print("moving file...")
    except:
        print("File exists in the folder.")
        pass

        
