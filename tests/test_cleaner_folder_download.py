import os
import shutil
import tempfile
import pytest
from cleaner_folder_download import Handler
from file_utilities import make_folder, move_to_new_corresponding_folder

@pytest.fixture
def temp_directory():
    # Create a temporary directory for testing
    temp_dir = tempfile.mkdtemp()

    #return to function as fixture.
    yield temp_dir

    # Remove the temporary directory after testing
    shutil.rmtree(temp_dir)

def test_on_modified_code_file(temp_directory, monkeypatch):
    handler = Handler()

    # Set up a temporary code file
    code_file = os.path.join(temp_directory, 'test_code.py')
    with open(code_file, 'w') as f:
        f.write("print('Hello, World!')")

    #Create with 'type' new class of unique line (name_of_class=Event, inherance=object, args=('src_path', 'is_directory') instance class too.)
    event = type('Event', (object,), {'src_path': code_file, 'is_directory': False})

    # Mock the make_folder and move_to_new_corresponding_folder functions
    def mock_make_folder(folder_name):
        assert folder_name == 'code'
        return os.path.join(temp_directory, 'code')

    def mock_move_to_new_corresponding_folder(event, path_to_folder):
        assert event.src_path == code_file
        assert path_to_folder == os.path.join(temp_directory, 'code')

    # Patch the functions
    monkeypatch.setattr('cleaner_folder_download.make_folder', mock_make_folder)
    monkeypatch.setattr('cleaner_folder_download.move_to_new_corresponding_folder', mock_move_to_new_corresponding_folder)

    # Ensure is_code_file returns True for testing purposes
    monkeypatch.setattr('cleaner_folder_download.is_code_file', lambda x: True)

    # Call the on_modified method
    handler.on_modified(event)

    # Assert that make_folder and move_to_new_corresponding_folder were called with the correct arguments
    # (Assertions are done within the mocked functions)

