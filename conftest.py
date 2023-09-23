import pytest
import os
from PIL import Image
import time

directory = './tmp'

def remove_dir(top: str) -> None:
    """
    Deletes all files and directories within a given directory.

    Args:
        top: A string representing the path to the directory to be deleted.

    Returns:
        None
    """
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            os.remove(file_path)
        for name in dirs:
            dir_path = os.path.join(root, name)
            os.rmdir(dir_path)
    os.rmdir(top)

def create_card(number_of_cards: int) -> None:
    """
    Create a specified number of image files as placeholders.

    Args:
        number_of_cards: An integer representing the number of image files to be created.

    Returns:
        None
    """
    for i in range(number_of_cards):
        hierarchy = 'major_arcana' if 'minor_arcana' else 'major_arcana'
        img = Image.new('RGB', (100, 100))
        img.save(f'{directory}/{hierarchy}_{i}.png')
        

def pytest_configure():
    # Your presetup code here
    print("Presetup code runs before any test")
    os.mkdir(directory)
    create_card(72)

def pytest_unconfigure():
    remove_dir(directory)
    print("Post-presetup code runs after all tests")