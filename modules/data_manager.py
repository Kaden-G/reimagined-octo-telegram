import json
import random

class DataManager:
    def __init__(self):
        # Load all exercise data
        self.exercises_upper = self.load_data('data/exercises_upper.json')
        self.exercises_leg = self.load_data('data/exercises_leg.json')
        self.exercises_full = self.load_data('data/exercises_full.json')
        self.quotes = self.load_data('data/quotes.json')  # Assuming your quotes are stored in a JSON file
        self.image_paths = self.load_data('data/image_paths.json')  # Load image paths for characters

    def load_data(self, file_path):
        # Load the JSON file data
        with open(file_path, 'r') as file:
            return json.load(file)
    
    def get_random_exercise(self):
        # Randomly select one exercise from each list
        upper_exercise = random.choice(self.exercises_upper['upper'])
        leg_exercise = random.choice(self.exercises_leg['leg'])
        full_body_exercise = random.choice(self.exercises_full['full_body'])

        # Return a dictionary of selected exercises
        return {
            "upper_body": upper_exercise,
            "leg": leg_exercise,
            "full_body": full_body_exercise
        }
