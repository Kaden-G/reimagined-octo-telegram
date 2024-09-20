import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from modules.data_manager import DataManager
from modules.exercise_generator import ExerciseGenerator
from modules.quote_generator import QuoteGenerator
from modules.image_handler import ImageHandler

class CalisthenicsRouletteApp:
    """
    This is the main class for the ThreatLevelCalisthenics application.
    It handles user inputs, displays the generated workout routines,
    and shows the selected character's themed image and quote.
    """
    
    def __init__(self, root):
        """
        Initializes the main application window and components.
        
        :param root: The root Tkinter window.
        """
        self.root = root
        self.root.title("Calisthenics Roulette")
        
        # Initialize data manager and helper classes
        self.data_manager = DataManager()
        self.exercise_generator = ExerciseGenerator(self.data_manager)
        self.quote_generator = QuoteGenerator(self.data_manager)
        self.image_handler = ImageHandler(self.data_manager)

        # Set up the user interface
        self.setup_ui()

    def setup_ui(self):
        """
        Set up the user interface, including input fields and display areas.
        """
        # Number Selection
        number_label = tk.Label(self.root, text="Choose a number (1-10):")
        number_label.pack(pady=5)
        
        self.number_var = tk.IntVar()
        self.number_spinbox = tk.Spinbox(self.root, from_=1, to=10, textvariable=self.number_var, width=5)
        self.number_spinbox.pack(pady=5)
        
        # Theme Selection (Character Dropdown)
        theme_label = tk.Label(self.root, text="Choose a character:")
        theme_label.pack(pady=5)
        
        self.theme_var = tk.StringVar()
        characters = list(self.data_manager.quotes.keys())  # Get character names from the quotes data
        self.theme_dropdown = ttk.Combobox(self.root, textvariable=self.theme_var, values=characters, state='readonly')
        self.theme_dropdown.pack(pady=5)
        
        # Generate Button
        generate_button = tk.Button(self.root, text="Generate Routine", command=self.generate_routine)
        generate_button.pack(pady=10)
        
        # Results Frame (for displaying image, quote, and exercises)
        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(pady=10)
        
        # Image Label (for character image)
        self.image_label = tk.Label(self.results_frame)
        self.image_label.grid(row=0, column=0, padx=10)
        
        # Quote Label (for character quote)
        self.quote_label = tk.Label(self.results_frame, wraplength=300, justify="left")
        self.quote_label.grid(row=0, column=1, padx=10)
        
        # Exercises Text (for exercise list)
        self.exercises_text = tk.Text(self.results_frame, height=10, width=50)
        self.exercises_text.grid(row=1, column=0, columnspan=2, pady=10)
        self.exercises_text.config(state=tk.DISABLED)
        
        # Control Buttons (Reset and Exit)
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(pady=5)
        
        reset_button = tk.Button(controls_frame, text="Reset", command=self.reset_game)
        reset_button.pack(side=tk.LEFT, padx=5)
        
        exit_button = tk.Button(controls_frame, text="Exit", command=self.exit_game)
        exit_button.pack(side=tk.LEFT, padx=5)

    def generate_routine(self):
        """
        Generates the workout routine, quote, and image based on user input.
        """
        # Get user inputs
        number = self.number_var.get()
        character = self.theme_var.get()
        
        # Validate that a character has been selected
        if not character:
            messagebox.showwarning("Input Error", "Please select a character.")
            return
        
        # Determine if the number is odd or even to choose focus area
        focus_area = 'leg' if number % 2 != 0 else 'upper'
        
        # Generate exercises
        exercises = self.exercise_generator.generate_exercises(focus_area, number)
        
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
        for exercise, reps in exercises:
            self.exercises_text.insert(tk.END, f"{exercise['name']} - {reps} reps\n{exercise['instructions']}\n\n")
        self.exercises_text.config(state=tk.DISABLED)  # Disable editing of text

    def reset_game(self):
        """
        Resets the game UI to its initial state.
        """
        self.number_var.set(1)
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
