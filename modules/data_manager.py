import json
import os

class DataManager:
    """
    This class handles loading and managing the data (exercises, quotes, and images) from JSON files.
    """
    
    def __init__(self, data_dir='data'):
        """
        Initializes the DataManager class.
        Loads the exercise, quote, and image data from the specified directory.

        :param data_dir: The directory where the JSON files are located (default: 'data').
        """
        self.data_dir = data_dir
        # Load leg and upper body exercises
        self.exercises_leg = self.load_data('exercises_leg.json')
        self.exercises_upper = self.load_data('exercises_upper.json')
        # Load character quotes
        self.quotes = self.load_data('quotes.json')
        # Load image paths
        self.image_paths = self.load_data('image_paths.json')

    def load_data(self, filename):
        """
        Loads data from a JSON file and returns it as a Python dictionary.

        :param filename: The name of the JSON file to load (e.g., 'exercises_leg.json').
        :return: A dictionary containing the loaded data.
        """
        path = os.path.join(self.data_dir, filename)
        try:
            with open(path, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return {}
