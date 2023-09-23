
# Generated by CodiumAI
from tarot import Tarot
import pytest
import os

directory = 'tmp'

class TestTarot:
    # Draw one card from library
    def test_draw_one_card_from_library(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Draw one card from the library
        tarot.draw(1)

        # Check if the drawn_cards list has one card
        assert len(tarot.drawn_cards) == 1


    # Draw multiple cards from library
    def test_draw_multiple_cards_from_library(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Generate the library with the default path
        tarot.generate_library()

        # Draw multiple cards from the library
        tarot.draw(3)

        # Check if the number of drawn cards is equal to the specified number
        assert len(tarot.drawn_cards) == 3


    # Show image of a card
    def test_show_image_of_card(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Draw a card from the library
        tarot.draw()

        # Get the name of the drawn card
        card_name = tarot.drawn_cards[0]

        # Show the image of the drawn card
        tarot.show(card_name)


    # Generate library with default path
    def test_generate_library_with_default_path(self):
        tarot = Tarot(directory)
        tarot.generate_library()
        assert tarot.library != ""


    # Load library from file
    def test_load_library_from_file(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Check if the library is not empty
        assert tarot.library != ""


    # Draw more cards than in the deck
    def test_draw_more_cards_than_in_deck(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Generate the library with the default path
        tarot.generate_library()

        # Try to draw more cards than in the deck
        with pytest.raises(ValueError):
            tarot.draw(100)


    # Draw negative number of cards
    def test_draw_negative_number_of_cards(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Check if drawing a negative number of cards raises a ValueError
        with pytest.raises(ValueError):
            tarot.draw(-1)


    # Draw one card from an empty deck
    def test_draw_one_card_from_empty_deck(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Clean up deck
        tarot.library = []

        # Draw one card from the library
        with pytest.raises(ValueError):
            tarot.draw(1)

        # Check if the drawn_cards list is empty
        assert len(tarot.drawn_cards) == 0


    # Save library to file
    def test_save_library_to_file(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Save the library to a file
        tarot.save_library()

        # Check if the library file exists
        assert os.path.isfile(tarot.library_file)


    # Show image of a non-existent card
    def test_show_image_of_nonexistent_card(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Draw a card from the library
        tarot.draw()

        # Get the name of the drawn card
        card_name = tarot.drawn_cards[0]

        # Remove the card from the library
        os.remove(f'{directory}/{card_name}')

        # Show the image of the non-existent card
        with pytest.raises(ValueError):
            tarot.show(card_name)


    # Draw zero cards
    def test_draw_zero_cards(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Draw zero cards from the library
        with pytest.raises(ValueError):
            tarot.draw(0)


    # Load non-existent library file
    def test_load_non_existent_library_file(self):
        # Create an instance of the Tarot class with a non-existent library file
        tarot = Tarot(directory)

        # Check if the library is generated and not empty
        assert tarot.library != ""


    # Draw all cards from the deck
    def test_draw_all_cards_from_deck(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Generate the library with the default path
        tarot.generate_library()

        # Draw all cards from the deck
        tarot.draw(len(tarot.library))

        # Check if the number of drawn cards is equal to the number of cards in the library
        assert len(tarot.drawn_cards) == len(tarot.library)


    # Retrieve major hierarchy and card name from file name
    def test_retrieve_major_hierarchy_and_card_name_from_file_name(self):
        # Create an instance of the Tarot class
        tarot = Tarot(directory)

        # Test with a file name that matches the pattern
        file_name = "major_arcana_0.jpg"
        hierarchy, card_name = tarot.retrieve_name(file_name)
        assert hierarchy == "major"
        assert card_name == "0"

        # Test with a file name that does not match the pattern
        file_name = "minor_arcana_card.jpg"
        hierarchy, card_name = tarot.retrieve_name(file_name)
        assert hierarchy != ""
        assert card_name != ""

