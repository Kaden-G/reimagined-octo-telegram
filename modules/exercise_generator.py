import random

class ExerciseGenerator:
    """
    This class is responsible for generating a random set of exercises based on user input.
    It chooses exercises from either a leg-focused or upper body-focused list, and assigns a random number
    of repetitions for each exercise.
    """
    
    def __init__(self, data_manager):
        """
        Initializes the ExerciseGenerator class.
        It requires an instance of DataManager to access exercise data.

        :param data_manager: An instance of the DataManager class that provides access to exercise data.
        """
        self.data_manager = data_manager

    def generate_exercises(self, focus_area, number):
        """
        Generates a list of three random exercises from either the leg-focused or upper body-focused list.
        Each exercise will be assigned a random number of repetitions between 5 and 15.

        :param focus_area: A string that indicates which type of exercises to generate ('leg' or 'upper').
        :param number: The number chosen by the user, which is used to decide the repetition range.
        :return: A list of tuples, where each tuple contains an exercise dictionary and the assigned number of repetitions.
        """
        # Select the appropriate list of exercises based on the focus area ('leg' or 'upper')
        if focus_area == 'leg':
            exercises = self.data_manager.exercises_leg['leg']
        else:
            exercises = self.data_manager.exercises_upper['upper']
        
        # Randomly select 3 unique exercises from the chosen list
        selected_exercises = random.sample(exercises, 3)
        
        # Generate a random number of repetitions between 5 and 15 for each exercise
        repetitions = [random.randint(5, 15) for _ in range(3)]
        
        # Return a list of tuples, where each tuple contains an exercise and its repetitions
        return list(zip(selected_exercises, repetitions))