import os
import shutil
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# File type categories
categories = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documents": [".pdf", ".doc", ".docx"],
    "scripts": [".py", ".sh", ".js"],
    "text": [".txt", ".md"],
    "data": [".csv", ".json", ".xml"]
}

def organize_folder(folder_path):
    print("===== FILE ORGANIZER =====")
    print("Organizing:", folder_path)
    print("Started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("")

    # Check folder exists
    if not os.path.exists(folder_path):
        print("ERROR: Folder not found!")
        logging.error("Folder not found: " + folder_path)
        return

    # Create category folders
    for category in categories:
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            logging.info("Created folder: " + category)

    # Move files
    moved = 0
    skipped = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get file extension
        ext = os.path.splitext(filename)[1].lower()

        # Find category
        moved_file = False
        for category, extensions in categories.items():
            if ext in extensions:
                destination = os.path.join(folder_path, category, filename)
                try:
                    shutil.move(file_path, destination)
                    print("Moved:", filename, "→", category)
                    logging.info("Moved: " + filename + " → " + category)
                    moved += 1
                    moved_file = True
                    break
                except Exception as e:
                    print("ERROR moving", filename, ":", str(e))
                    logging.error("Error moving: " + filename)

        if not moved_file:
            print("Skipped:", filename, "(unknown type)")
            logging.info("Skipped: " + filename)
            skipped += 1

    print("")
    print("===== DONE =====")
    print("Files moved:", moved)
    print("Files skipped:", skipped)
    logging.info("Complete - Moved: " + str(moved) + " Skipped: " + str(skipped))

# Run organizer
organize_folder("/home/frida/test_folder")
