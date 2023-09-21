import re
from PIL import Image
import random
import json
import os

"""
A class for generating a library of tarot cards from a given deck directory.

Args:
    deck_directory (str): The directory path where the tarot card images are located.

Attributes:
    deck_directory (str): The directory path where the tarot card images are located.
    library (str): The library of tarot cards as a JSON string.

Methods:
    __init__(self, deck_directory: str): Initializes the class with the deck directory.
    generate_library(self, path: str = '') -> str: Generates a library of tarot cards and returns it as a JSON string.
    save_library(self): Saves the library to a file.
    retrieve_name(self, file: str) -> str: Retrieves the major or minor hierarchy and card name from a given file name.
    draw(self, number = 1): Randomly draws a specified number of cards from the library.
    show(self, card): Shows the image of a card.
"""
"""
A class for generating a library of tarot cards from a given deck directory.

Args:
    deck_directory (str): The directory path where the tarot card images are located.

Attributes:
    deck_directory (str): The directory path where the tarot card images are located.
    library (str): The library of tarot cards as a JSON string.

Methods:
    __init__(self, deck_directory: str): Initializes the class with the deck directory.
    generate_library(self, path: str = '') -> str: Generates a library of tarot cards and returns it as a JSON string.
    save_library(self): Saves the library to a file.
    retrieve_name(self, file: str) -> str: Retrieves the major or minor hierarchy and card name from a given file name.
    draw(self, number = 1): Randomly draws a specified number of cards from the library.
    show(self, card): Shows the image of a card.
"""
"""
A class for generating a library of tarot cards from a given deck directory.

Args:
    deck_directory (str): The directory path where the tarot card images are located.

Attributes:
    deck_directory (str): The directory path where the tarot card images are located.
    library (str): The library of tarot cards as a JSON string.

Methods:
    __init__(self, deck_directory: str): Initializes the class with the deck directory.
    generate_library(self, path: str = '') -> str: Generates a library of tarot cards and returns it as a JSON string.
    save_library(self): Saves the library to a file.
    retrieve_name(self, file: str) -> str: Retrieves the major or minor hierarchy and card name from a given file name.
    draw(self, number = 1): Randomly draws a specified number of cards from the library.
    show(self, card): Shows the image of a card.
"""
class Tarot:
    """
    A class for generating a library of tarot cards from a given deck directory.

    Args:
        deck_directory (str): The directory path where the tarot card images are located.

    Attributes:
        deck_directory (str): The directory path where the tarot card images are located.
        library (str): The library of tarot cards as a JSON string.

    Methods:
        __init__(self, deck_directory: str): Initializes the class with the deck directory.
        generate_library(self, path: str = '') -> str: Generates a library of tarot cards and returns it as a JSON string.
        save_library(self): Saves the library to a file.
        retrieve_name(self, file: str) -> str: Retrieves the major or minor hierarchy and card name from a given file name.
        draw(self, number = 1): Randomly draws a specified number of cards from the library.
        show(self, card): Shows the image of a card.
    """

    def __init__(self, deck_directory: str):
        """
        Initializes the Tarot class with the deck directory.

        Args:
            deck_directory (str): The directory path where the tarot card images are located.
        """
        self.deck_directory = deck_directory
        self.library_file = f'{self.deck_directory}/library.json'
        self.drawn_cards = []

        if not os.path.isfile(self.library_file):
            self.generate_library()

        self.load_library()

    def generate_library(self, path: str = '') -> str:
        """
        Generates a library of tarot cards and returns it as a JSON string.

        Args:
            path (str): The path to the deck directory. If not provided, uses the instance's deck_directory.

        Returns:
            str: The library of tarot cards as a JSON string.
        """
        if not path:
            path = self.deck_directory

        library = {}

        if os.path.isdir(path):
            for file in os.listdir(path):
                hierarchy, card_name = self.retrieve_name(file)
                library[file] = {'hierarchy': hierarchy, 'arcane': card_name}
        
        self.library = json.dumps(library, indent=2)

    def load_library(self):
        """
        Loads the library from a file.
        """
        with open(self.library_file, "r") as json_file:
            self.library = json.load(json_file)

    def save_library(self):
        """
        Saves the library to a file.
        """
        with open(self.library_file, "w") as json_file:
            json.dump(self.library, json_file, indent=2)

    def retrieve_name(self, file: str) -> str:
        """
        Retrieves the major or minor hierarchy and card name from a given file name.

        Args:
            file (str): The file name of the tarot card image.

        Returns:
            str: The major or minor hierarchy and card name.
        """
        hierarchy = ''
        card_name = ''

        # Extract the hierarchy and card name from the file name
        match = re.search(r'([A-Za-z]+)_([A-Za-z]+)_(.+)\.', file)

        if match:
            hierarchy = match.group(1)
            card_name = match.group(3).replace("_"," ")
        return hierarchy, card_name
    
    def show(self, card):
        """
        Shows the image of a card.

        Args:
            card: The name of the card to show.
        """
        file_path = f'{self.deck_directory}/{card}'
        img = Image.open(file_path)
        image_size = img.size
        image_size = image_size[0]//2, image_size[1]//2
        card = img.resize(image_size)
        card.show()

    def draw(self, number = 1):
        """
        Randomly draws a specified number of cards from the library.

        Args:
            number (int): The number of cards to draw. Defaults to 1.
        """
        if number > len(self.library):
            raise ValueError('Number of cards bigger than deck!')

        deck = list(self.library)

        for i in range(number):
            draw_card = random.choice(deck)
            self.drawn_cards.append(draw_card)
            deck.remove(draw_card)
