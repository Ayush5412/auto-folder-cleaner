# Automatic File Sorter
#### A simple, highly-configurable Python script that runs in the background to automatically organize files in a specified folder (e.g., your Downloads folder) into categorized subdirectories.

### Features
#### Continuous Monitoring: The script runs indefinitely, checking for new files at a set interval.
#### Customizable Rules: Easily define which file extensions go into which folders by editing a simple dictionary.
#### Cross-Platform: Works on Windows, macOS, and Linux.
#### Lightweight: Uses minimal system resources and has no external library dependencies.
#### Automatic Folder Creation: If a destination folder doesn't exist, the script creates it for you.
#### Error Handling: Gracefully handles common errors like a missing target directory.


## Requirements
Python 3 installed and added to your system's PATH.


Setup & Configuration
Clone or Download:
Clone this repository or download the file_sorter.py script to your local machine.

Set the Target Folder:
Open the file_sorter.py script in a text editor. You must change the DOWNLOADS_PATH variable to the full path of the folder you want to organize.

# --- IMPORTANT: How to set your path ---
### Windows: Use a raw string by adding an 'r' before the path.
#### DOWNLOADS_PATH = r"C:\Users\YourUsername\Downloads"

### macOS:
#### DOWNLOADS_PATH = "/Users/YourUsername/Downloads"

### Linux:
#### DOWNLOADS_PATH = "/home/YourUsername/Downloads"

Customize Sorting Rules (Optional):
You can change how files are sorted by editing the FOLDER_MAPPING dictionary. Add new extensions to the tuples or create entirely new categories.

FOLDER_MAPPING = {
    # Add a new category for design files
    (".psd", ".ai", ".fig"): "Design Files",

    # Add more extensions to an existing category
    (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic"): "Images",

    # ... other categories
}

Usage
Once configured, you can run the script from your terminal:

python file_sorter.py

The script will start monitoring the specified folder. You can minimize the terminal window and let it run in the background. To stop the script, return to the terminal and press Ctrl+C.

How to Run on Startup
For a true "set it and forget it" experience, you can configure the script to run automatically when your computer starts.

Windows
Create a Batch File: Create a new text file and add the line below, replacing the path with the location of your script. Save it as run_sorter.bat.

@echo off
python "C:\path\to\your\file_sorter.py"

Open Startup Folder: Press Win + R, type shell:startup, and press Enter.

Add Script: Move the run_sorter.bat file into this folder.

macOS
Go to Login Items: Navigate to System Settings > General > Login Items.

Add Script: Under "Open at Login," click the + button and select your file_sorter.py script.

Linux (GNOME/Ubuntu)
Open Startup Applications: Search for and open the "Startup Applications" utility.


Contributing
Contributions are welcome! If you have ideas for improvements or find a bug, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
