# Tarot
## Summary
The `Tarot` class is used to generate a library of tarot cards from a given deck directory. It allows for the retrieval of card names and hierarchies, as well as the ability to draw and show tarot cards.

## Example Usage
```python
# Create an instance of the Tarot class with the deck directory
tarot = Tarot('deck_directory')

# Generate the library of tarot cards
tarot.generate_library()

# Save the library to a file
tarot.save_library()

# Draw a random card from the library
card = tarot.draw()

# Show the image of the drawn card
tarot.show(card)
```

## Code Analysis
### Main functionalities
The main functionalities of the `Tarot` class are:
- Generating a library of tarot cards from a given deck directory
- Saving the library to a file
- Retrieving the major or minor hierarchy and card name from a given file name
- Drawing a specified number of cards from the library
- Showing the image of a card
___
### Methods
The `Tarot` class has the following methods:
- `__init__(self, deck_directory: str)`: Initializes the class with the deck directory
- `generate_library(self, path: str = '') -> str`: Generates a library of tarot cards and returns it as a JSON string
- `save_library(self)`: Saves the library to a file
- `retrieve_name(self, file: str) -> str`: Retrieves the major or minor hierarchy and card name from a given file name
- `draw(self, number = 1)`: Randomly draws a specified number of cards from the library
- `show(self, card)`: Shows the image of a card
___
### Fields
The `Tarot` class has the following fields:
- `deck_directory (str)`: The directory path where the tarot card images are located
- `library (str)`: The library of tarot cards as a JSON string
___
