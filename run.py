import os
import time
import shutil

# --- Configuration ---
# The folder to monitor (e.g., your Downloads folder)
# Windows: r"C:\Users\YourUsername\Downloads"
# macOS: "/Users/YourUsername/Downloads"
# Linux: "/home/YourUsername/Downloads"
DOWNLOADS_PATH = "C:\\Users\\Student\\Downloads" # !!! IMPORTANT: CHANGE THIS PATH !!!

# How often to check the folder, in seconds
CHECK_INTERVAL = 10

# Mapping of file extensions to folder names
# You can customize this to your liking
FOLDER_MAPPING = {
    # Images
    (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"): "Images",
    # Documents
    (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".csv"): "Documents",
    # Archives
    (".zip", ".rar", ".7z", ".tar", ".gz"): "Archives",
    # Audio
    (".mp3", ".wav", ".aac", ".flac"): "Audio",
    # Video
    (".mp4", ".mov", ".avi", ".mkv"): "Videos",
    # Code & Scripts
    (".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".sh"): "Code",
    # Executables & Installers
    (".exe", ".msi", ".dmg", ".pkg"): "Installers",
    # Other
    # All other file types will be moved to a folder named "Other"
}

# --- Main Script Logic ---

def get_folder_for_extension(extension):
    """Finds the target folder name for a given file extension."""
    for extensions, folder_name in FOLDER_MAPPING.items():
        if extension.lower() in extensions:
            return folder_name
    return "Other" # Default folder for unmapped file types

def sort_files():
    """
    Scans the DOWNLOADS_PATH for files and moves them to their respective folders.
    """
    print(f"Scanning '{DOWNLOADS_PATH}'...")
    try:
        # List all entries in the directory
        for filename in os.listdir(DOWNLOADS_PATH):
            source_path = os.path.join(DOWNLOADS_PATH, filename)

            # Check if it's a file and not a directory
            if os.path.isfile(source_path):
                # Get the file extension
                _, file_extension = os.path.splitext(filename)

                if not file_extension: # Skip files without an extension
                    continue

                # Determine the destination folder
                destination_folder_name = get_folder_for_extension(file_extension)
                destination_folder_path = os.path.join(DOWNLOADS_PATH, destination_folder_name)

                # Create the destination folder if it doesn't exist
                if not os.path.exists(destination_folder_path):
                    print(f"Creating folder: '{destination_folder_path}'")
                    os.makedirs(destination_folder_path)

                # Move the file
                destination_path = os.path.join(destination_folder_path, filename)
                print(f"Moving '{filename}' to '{destination_folder_name}' folder.")
                shutil.move(source_path, destination_path)

    except FileNotFoundError:
        print(f"Error: The directory '{DOWNLOADS_PATH}' was not found.")
        print("Please update the DOWNLOADS_PATH variable in the script.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("--- Automatic File Sorter Started ---")
    print(f"Monitoring: {DOWNLOADS_PATH}")
    print(f"Press Ctrl+C to stop the script.")

    # This creates an infinite loop to keep the script running
    try:
        while True:
            sort_files()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n--- Script stopped by user. ---")

