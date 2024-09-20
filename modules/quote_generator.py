import random

class QuoteGenerator:
    """
    This class is responsible for retrieving a random quote from a specified character.
    It uses the character name to find a list of quotes and randomly selects one.
    """
    
    def __init__(self, data_manager):
        """
        Initializes the QuoteGenerator class.
        It requires an instance of DataManager to access the quotes data.

        :param data_manager: An instance of the DataManager class that provides access to quote data.
        """
        self.data_manager = data_manager

    def get_random_quote(self, character):
        """
        Retrieves a random quote for the specified character from the data loaded by the DataManager.

        :param character: A string representing the character's name (e.g., 'Michael Scott').
        :return: A randomly selected quote for the character, or a default message if no quotes are available.
        """
        # Retrieve the list of quotes for the specified character
        quotes = self.data_manager.quotes.get(character, [])
        
        # If quotes are available, randomly choose one. Otherwise, return a default message.
        if quotes:
            return random.choice(quotes)
        else:
            return "No quotes available for this character."