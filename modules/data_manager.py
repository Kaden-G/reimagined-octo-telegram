import json
import os

class DataManager:
    """
    This class handles loading and managing the data (exercises and quotes) from JSON files.
    It loads data for leg and upper body exercises, as well as character quotes.
    """
    
    def __init__(self, data_dir='data'):
        """
        Initializes the DataManager class.
        Loads the exercise and quote data from the specified directory.

        :param data_dir: The directory where the JSON files are located (default: 'data').
        """
        self.data_dir = data_dir
        # Load leg exercises from the 'exercises_leg.json' file
        self.exercises_leg = self.load_data('exercises_leg.json')
        # Load upper body exercises from the 'exercises_upper.json' file
        self.exercises_upper = self.load_data('exercises_upper.json')
        # Load character quotes from the 'quotes.json' file
        self.quotes = self.load_data('quotes.json')

    def load_data(self, filename):
        """
        Loads data from a JSON file and returns it as a Python dictionary.

        :param filename: The name of the JSON file to load (e.g., 'exercises_leg.json').
        :return: A dictionary containing the loaded data.
        """
        # Get the full path of the file by joining the directory and filename
        path = os.path.join(self.data_dir, filename)
        
        # Open the file and load its content as a dictionary
        with open(path, 'r') as file:
            return json.load(file)