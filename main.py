import tkinter as tk
from PIL import Image, ImageTk
import random
from modules.data_manager import DataManager
from modules.exercise_generator import ExerciseGenerator
from modules.quote_generator import QuoteGenerator
from modules.image_handler import ImageHandler
from modules.ui_manager import UIManager  # Importing the UI Manager

class CalisthenicsRouletteApp:
    """
    This is the main class for the Calisthenics Roulette application.
    It handles user inputs, generates the workout routines, and manages the application flow.
    """
    
    def __init__(self, root):
        """
        Initializes the main application and components.
        
        :param root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Calisthenics Roulette")
        
        # Initialize data manager and helper classes
        self.data_manager = DataManager()
        self.exercise_generator = ExerciseGenerator(self.data_manager)
        self.quote_generator = QuoteGenerator(self.data_manager)
        self.image_handler = ImageHandler(self.data_manager)

        # Initialize the UIManager to handle UI setup
        self.ui_manager = UIManager(root, self)

    def generate_routine(self):
        """
        Generates a random workout routine, quote, and image based on user input.
        """
        # Get user inputs
        character = self.theme_var.get()
        
        # Validate that a character has been selected
        if not character:
            tk.messagebox.showwarning("Input Error", "Please select a character.")
            return

        # Get random exercises from each JSON list (upper, leg, full-body)
        try:
            upper_exercise = random.choice(self.data_manager.exercises_upper['upper'])
            leg_exercise = random.choice(self.data_manager.exercises_leg['leg'])
            full_body_exercise = random.choice(self.data_manager.exercises_full['full_body'])
        except (KeyError, IndexError):
            tk.messagebox.showerror("Data Error", "There was an issue loading the exercises.")
            return
        
        # Generate a random quote
        quote = self.quote_generator.get_random_quote(character)
        
        # Load the character's themed image
        image = self.image_handler.load_image(character)
        
        # Update the UI with the generated results
        # Update Image
        if image:
            self.image_label.config(image=image)
            self.image_label.image = image  # Keep a reference to avoid garbage collection
        else:
            self.image_label.config(text="Image not available.")
        
        # Update Quote
        self.quote_label.config(text=quote)
        
        # Update Exercise List
        self.exercises_text.config(state=tk.NORMAL)
        self.exercises_text.delete('1.0', tk.END)  # Clear previous content
        self.exercises_text.insert(tk.END, f"Upper Body: {upper_exercise['name']} - {upper_exercise['instructions']}\n\n")
        self.exercises_text.insert(tk.END, f"Leg: {leg_exercise['name']} - {leg_exercise['instructions']}\n\n")
        self.exercises_text.insert(tk.END, f"Full Body: {full_body_exercise['name']} - {full_body_exercise['instructions']}\n\n")
        self.exercises_text.config(state=tk.DISABLED)  # Disable editing of text

    def reset_game(self):
        """
        Resets the game UI to its initial state.
        """
        self.theme_var.set('')
        self.image_label.config(image='', text='')
        self.quote_label.config(text='')
        self.exercises_text.config(state=tk.NORMAL)
        self.exercises_text.delete('1.0', tk.END)
        self.exercises_text.config(state=tk.DISABLED)

    def exit_game(self):
        """
        Exits the application.
        """
        self.root.quit()

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalisthenicsRouletteApp(root)
    root.mainloop()
