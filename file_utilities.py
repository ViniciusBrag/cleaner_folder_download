import os
import shutil


def extension_type(event):
    try:
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
    return extension_type(event) == "mp3"


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
    return extension_type(event) in ("exe", "msi", "deb")


def make_folder(foldername):
    os.chdir(os.getenv("DIRECTORY_OF_CLEANER"))
    folder_path = os.path.join(os.getcwd(), str(foldername))
    if os.path.exists(folder_path):
        print("Folders already exists, skipping creation")
        return False
    else:
        os.mkdir(str(folder_path))
        return True


def move_to_new_corresponding_folder(event, path_to_new_folder):
    try:
        shutil.move(event.src_path, path_to_new_folder)
        print("moving file...")
    except:
        if (shutil.Error, shutil.SameFileError):
            try:
                repeat_files = os.mkdir('repeat-files')
                shutil.move(event.src_path, repeat_files)
            except (shutil.ExecError, shutil.Error):
                print(shutil.Error)
