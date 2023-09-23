# Tarot
## Summary
The `Tarot` class is used to generate a library of tarot cards from a given deck directory. It provides methods to generate the library, save it to a file, load it from a file, draw cards from the library, show the image of a card, and retrieve the hierarchy and card name from a file name.

## Example Usage
```python
# Create an instance of the Tarot class with the deck directory
tarot = Tarot(deck_directory)

# Generate the library of tarot cards
tarot.generate_library()

# Save the library to a file
tarot.save_library()

# Load the library from a file
tarot.load_library()

# Draw a specified number of cards from the library
tarot.draw(number)

# Show the image of a card
tarot.show(card)

# Retrieve the hierarchy and card name from a file name
hierarchy, card_name = tarot.retrieve_name(file_name)
```

## Code Analysis
### Main functionalities
The main functionalities of the `Tarot` class are:
- Generating a library of tarot cards from a given deck directory
- Saving the library to a file
- Loading the library from a file
- Drawing a specified number of cards from the library
- Showing the image of a card
- Retrieving the hierarchy and card name from a file name
___
### Methods
The `Tarot` class has the following methods:
- `__init__(self, deck_directory: str)`: Initializes the class with the deck directory
- `generate_library(self, path: str = '') -> str`: Generates a library of tarot cards and returns it as a JSON string
- `save_library(self)`: Saves the library to a file
- `load_library(self)`: Loads the library from a file
- `retrieve_name(self, file: str) -> str`: Retrieves the major or minor hierarchy and card name from a given file name
- `draw(self, number=1)`: Randomly draws a specified number of cards from the library
- `show(self, card)`: Shows the image of a card
___
### Fields
The `Tarot` class has the following fields:
- `deck_directory`: The directory path where the tarot card images are located
- `library_file`: The file path of the library file
- `drawn_cards`: A list to store the drawn cards from the library
- `library`: The library of tarot cards as a JSON string
___
