Introduction
Threat Level Calisthenics is a fun and engaging desktop application designed to provide mini workout routines to keep us moving during the day. 
Your most beloved characters from the TV show The Office are there to motivate you. 

Features:
  Character-Themed Workouts: Choose from a list of iconic The Office characters to generate a personalized workout routine.
  Dynamic Exercise Selection: Based on your input number, receive a tailored set of exercises focusing on either upper body or legs.
  Inspirational Quotes: Each workout is accompanied by a motivational quote from your selected character to keep you inspired.
  Visual Motivation: Display themed images of your chosen character to enhance your workout experience.
  Streak Tracker: Track your consecutive workout days to stay motivated and achieve your fitness goals.
  Multi-User Support: Allow family members to create individual profiles and track their unique workout routines and streaks.

Technology Stack:
  Programming Language: Python 3.12
  GUI Framework: Tkinter
  Image Handling: Pillow (PIL)
  Data Storage: JSON files
  Cloud Services: AWS (optional for scaling and advanced features)

Installation Prerequisites
  Python 3.12 or higher installed on your machine.
  Git installed for version control.
  Virtual Environment setup to manage dependencies.

Steps
  Clone the Repository:

  bash
  Copy code
  git clone https://github.com/yourusername/CalisthenicsRoulette.git
  cd CalisthenicsRoulette

Set Up Virtual Environment:
It's recommended to use a virtual environment to manage project dependencies.

  bash
  Copy code
  python3 -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate

Install Dependencies:

  bash
  Copy code
  pip install -r requirements.txt

  If requirements.txt is not present, install dependencies manually:

  bash
  Copy code
  pip install Pillow

Verify Directory Structure:

Ensure the project directories are organized as follows:

CSS Copy code
ThreatLevelCalisthenics/
├── data/
│   ├── exercises_leg.json
│   ├── exercises_upper.json
│   ├── quotes.json
│   ├── image_paths.json
│   └── streak.json
├── images/
│   ├── Andrew_Bernard.png
│   ├── Angela_Martin.png
│   ├── ... (other character images)
├── modules/
│   ├── data_manager.py
│   ├── exercise_generator.py
│   ├── quote_generator.py
│   └── image_handler.py
├── main.py
├── README.md
└── requirements.txt

Add Character Images:

  Place your character images in the images/ directory, ensuring each image is named following the format Character_Name.png (e.g., Michael_Scott.png).

Usage
  Activate Virtual Environment:

  bash
  Copy code
  source env/bin/activate  # On Windows: env\Scripts\activate

Run the Application:

  bash
  Copy code
  python main.py

Generate Workout Routine:

Choose a Number (1-10): Determines the focus area (odd for legs, even for upper body).
Select a Character: Pick your favorite The Office character from the dropdown.
Click "Generate Routine": Receive a set of exercises, view an inspirational quote, and see the character's image.
Track Your Streak:

Daily Usage: The app tracks consecutive days you use it to generate workouts.
View Streak: Your current streak is displayed to motivate consistent workouts.
Reset or Exit:

Reset: Clears the current workout and selections.
Exit: Closes the application.

Project Structure:
css
Copy code
CalisthenicsRoulette/
├── data/
│   ├── exercises_leg.json
│   ├── exercises_upper.json
│   ├── quotes.json
│   ├── image_paths.json
│   └── streak.json
├── images/
│   ├── Andrew_Bernard.png
│   ├── Angela_Martin.png
│   ├── ... (other character images)
├── modules/
│   ├── data_manager.py
│   ├── exercise_generator.py
│   ├── quote_generator.py
│   └── image_handler.py
├── main.py
├── README.md
└── requirements.txt

Description
  data/: Contains all JSON files managing exercises, quotes, image paths, and streak data.
  images/: Stores all character images used in the application.
  modules/: Houses Python modules for data management, exercise generation, quote retrieval, and image handling.
  main.py: The main script that runs the application.
  requirements.txt: Lists all Python dependencies required for the project.
  README.md: This documentation file.
  Data Management
  Exercises
  Files:

  exercises_leg.json: Contains leg-focused exercises.
  exercises_upper.json: Contains upper body-focused exercises.

Structure:

json
Copy code
{
  "upper": [
    {
      "name": "Push-ups",
      "instructions": "Keep your back straight and lower your body until your chest nearly touches the floor."
    },
    // More exercises...
  ],
  "leg": [
    {
      "name": "Squats",
      "instructions": "Keep your back straight and lower your hips until your thighs are parallel to the floor."
    },
    // More exercises...
  ]
}
Quotes
File:

quotes.json: Contains 5 quotes for each character.
Structure:

json
Copy code
{
  "Andrew_Bernard": [
    "I wish there was a way to know you’re in the good old days before you’ve actually left them.",
    "Rit dit dit di doo!",
    "I’m always thinking one step ahead, like a... carpenter... that makes stairs.",
    "Sorry I annoyed you with my friendship.",
    "I went to Cornell. Ever heard of it?"
  ],
  // More characters...
}
Images
File:

image_paths.json: Maps each character to their respective image file.
Structure:

json
Copy code
{
  "Andrew_Bernard": "images/Andrew_Bernard.png",
  "Angela_Martin": "images/Angela_Martin.png",
  "Creed_Bratton": "images/Creed_Bratton.png",
  // More characters...
}
Streak Tracker
File:

streak.json: Tracks user streaks.
Structure:

json
Copy code
{
  "users": {
    "family_member_1": {
      "current_streak": 5,
      "last_used": "2024-04-25"
    },
    "family_member_2": {
      "current_streak": 3,
      "last_used": "2024-04-24"
    }
  }
}
User Authentication & Streak Tracker
To accommodate multiple family members, the app includes user authentication and a streak tracker. Users can create individual profiles, log in, and track their consecutive workout days.

Implementation
User Profiles:

Each user has a unique profile with their own streak data.
Profiles are managed locally using streak.json or via AWS services like DynamoDB for scalability.
Streak Tracking:

The app updates and displays the user's current streak each time they generate a workout routine.
Streak data is stored securely and updated daily based on usage.
Future Enhancements
AWS Integration:
AWS Cognito: For secure user authentication and management.
AWS DynamoDB: For scalable storage of user data and streaks.
AWS S3: For hosting images and other assets.
AWS Lambda & SNS: For sending workout reminders and motivational notifications.
Contributing
Contributions are welcome! If you'd like to enhance Calisthenics Roulette, please follow these steps:

Fork the Repository:

Click the "Fork" button at the top right of the repository page.
Clone Your Fork:

bash
Copy code
git clone https://github.com/yourusername/CalisthenicsRoulette.git
cd CalisthenicsRoulette
Create a New Branch:

bash
Copy code
git checkout -b feature/YourFeatureName
Make Your Changes:

Add new exercises, improve UI, fix bugs, etc.
Commit Your Changes:

bash
Copy code
git commit -m "Add feature: Your Feature Description"
Push to Your Fork:

bash
Copy code
git push origin feature/YourFeatureName
Create a Pull Request:

Navigate to the original repository and create a pull request from your forked repository.
Guidelines
Code Style: Follow PEP 8 guidelines for Python code.
Documentation: Update the README and comments in the code as necessary.
Testing: Ensure that new features are tested and do not break existing functionality.
License
This project is licensed under the MIT License.

Acknowledgements
The Office – For providing endless inspiration through beloved characters.
Pillow (PIL) – For powerful image processing capabilities.
Tkinter – For the user-friendly GUI framework.
OpenAI ChatGPT – For assisting in project development and troubleshooting.
