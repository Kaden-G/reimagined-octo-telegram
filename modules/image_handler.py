from PIL import Image, ImageTk
import os

class ImageHandler:
    """
    This class is responsible for loading images for the selected character.
    It retrieves image paths from a JSON file and loads the image using Pillow (PIL).
    """
    
    def __init__(self, data_manager, images_dir='images'):
        """
        Initializes the ImageHandler class.
        It requires an instance of DataManager to access image path data.

        :param data_manager: An instance of the DataManager class that provides access to image paths.
        :param images_dir: The directory where images are stored (default: 'images').
        """
        self.data_manager = data_manager
        self.images_dir = images_dir

    def get_image_path(self, character):
        """
        Retrieves the image path for the specified character.

        :param character: A string representing the character's name (e.g., 'Michael Scott').
        :return: The file path of the character's themed image.
        """
        # Retrieve the image path from the data manager's image mapping
        return self.data_manager.image_paths.get(character)

    def load_image(self, character, size=(200, 200)):
        """
        Loads and resizes the character's image using Pillow (PIL).

        :param character: The name of the selected character.
        :param size: A tuple specifying the desired image size (default: (200, 200)).
        :return: A Tkinter-compatible image object (PhotoImage).
        """
        # Get the image path for the selected character
        path = self.get_image_path(character)
        
        # Ensure the image exists, then load and resize it
        try:
            image = Image.open(path)
            image = image.resize(size, Image.ANTIALIAS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image for {character}: {e}")
            return None