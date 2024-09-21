import tkinter as tk
from tkinter import ttk

class UIManager:
    """
    This class handles the setup and styling of the user interface components.
    It separates UI-related logic from the main logic.
    """
    
    def __init__(self, root, app):
        """
        Initializes the UI components.

        :param root: The root Tkinter window.
        :param app: The main application object (CalisthenicsRouletteApp) for callback functions.
        """
        self.root = root
        self.app = app

        # Call the method to setup the UI
        self.setup_ui()

    def setup_ui(self):
        """
        Set up the user interface components, including input fields and display areas.
        """
        # Theme Selection (Character Dropdown)
        theme_label = tk.Label(self.root, text="Choose a character:")
        theme_label.pack(pady=5)
        
        self.app.theme_var = tk.StringVar()
        characters = list(self.app.data_manager.quotes.keys())  # Get character names from the quotes data
        self.app.theme_dropdown = ttk.Combobox(self.root, textvariable=self.app.theme_var, values=characters, state='readonly')
        self.app.theme_dropdown.pack(pady=5)
        
        # Generate Button
        generate_button = tk.Button(self.root, text="Generate Routine", command=self.app.generate_routine)
        generate_button.pack(pady=10)
        
        # Results Frame (for displaying image, quote, and exercises)
        self.app.results_frame = tk.Frame(self.root)
        self.app.results_frame.pack(pady=10)
        
        # Image Label (for character image)
        self.app.image_label = tk.Label(self.app.results_frame)
        self.app.image_label.grid(row=0, column=0, padx=10)
        
        # Quote Label (for character quote)
        self.app.quote_label = tk.Label(self.app.results_frame, wraplength=300, justify="left")
        self.app.quote_label.grid(row=0, column=1, padx=10)
        
        # Exercises Text (for exercise list)
        self.app.exercises_text = tk.Text(self.app.results_frame, height=10, width=50)
        self.app.exercises_text.grid(row=1, column=0, columnspan=2, pady=10)
        self.app.exercises_text.config(state=tk.DISABLED)
        
        # Control Buttons (Reset and Exit)
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(pady=5)
        
        reset_button = tk.Button(controls_frame, text="Reset", command=self.app.reset_game)
        reset_button.pack(side=tk.LEFT, padx=5)
        
        exit_button = tk.Button(controls_frame, text="Exit", command=self.app.exit_game)
        exit_button.pack(side=tk.LEFT, padx=5)
