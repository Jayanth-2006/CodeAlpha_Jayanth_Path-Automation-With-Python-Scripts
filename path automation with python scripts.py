import os
import shutil

source_dir = "C:/Users/user/Desktop/mixed_files"
dest_dir = "C:/Users/user/Desktop/sorted_files"

categories = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Archives": [".zip", ".rar"]
}

for category in categories.keys():
    os.makedirs(os.path.join(dest_dir, category), exist_ok=True)

for file in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file)
    if os.path.isfile(file_path):
        for category, extensions in categories.items():
            if any(file.endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(dest_dir, category, file))

print("Task Completed")