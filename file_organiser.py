import os
import shutil

source_folder = input("Enter folder path: ")

files = os.listdir(source_folder)

for file in files:
    if file.endswith(".jpg"):
        folder = "Images"
    elif file.endswith(".pdf"):
        folder = "PDFs"
    elif file.endswith(".mp3"):
        folder = "Music"
    else:
        folder = "Others"

    folder_path = os.path.join(source_folder, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(os.path.join(source_folder, file), folder_path)

print("Files organized successfully!")
