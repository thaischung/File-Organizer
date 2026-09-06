import os
import shutil
import time
import logging
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

# file paths user must complete before using 
user_dir_path = ""
dest_path_documents = "/Users/thais/Desktop/docs"
dest_path_images = "/Users/thais/Desktop/images"
dest_path_sounds = "/Users/thais/Desktop/sounds"
dest_path_videos = "/Users/thais/Desktop/videos"
dest_path_miscellaneous = "/Users/thais/Desktop/miscellaneous"

DOWNLOAD_TIME = 2 # temporary fix to handeling incomplete downloads

# document file supported extensions
document_extensions = [".doc", ".docx", ".odt", ".rtf", ".txt", ".xls", ".xlsx", ".ods", ".csv", ".ppt", ".pptx", ".odp", ".pdf", ".epub", ".md", ".tex", ".pages"]

# image file supported extensions 
image_extensions = [".jpeg", ".jpg", ".jfif", "pjpeg", ".pjp", ".gif", ".png", ".svg", ".bmp", ".tiff", ".tif", ".webp", ".ico", ".HEIC"]

# sound file supported extensions
sound_extensions = [".mp3", ".acc", ".ogg", ".wma", ".m4a", ".wav", ".aiff", ".flac"]

# video file supported extensions
video_extensions = [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm", ".mpeg", ".3gp", ".m4v"]

# miscellaneous files if no other supported extensions matches

# make the directories if they do not exist on the machine already 
os.makedirs(dest_path_documents, exist_ok=True)
os.makedirs(dest_path_images, exist_ok=True)
os.makedirs(dest_path_sounds, exist_ok=True)
os.makedirs(dest_path_videos, exist_ok=True)
os.makedirs(dest_path_miscellaneous, exist_ok=True)

class customEventHandler(FileSystemEventHandler): # subclass of the FileSystemEventHandler 

    def clean_folder(self): 
        self.print_start()
        with os.scandir(user_dir_path) as folder:
            for file in folder:
                if file.is_file():
                    # check the file types
                    file_name = file.name
                    self.check_type_and_sort(file_name)  

    def on_created(self, event):
        if event.src_path.endswith(".crdownload") or os.path.basename(event.src_path).startswith(".com.google.Chrome."):
            return

        with os.scandir(user_dir_path) as folder:
            for file in folder:
                if file.is_file():
                    # check the file types
                    file_name = file.name
                    self.check_type_and_sort(file_name)

    def check_type_and_sort(self, file_name): 
        _, ext = os.path.splitext(file_name)

        if ext in document_extensions:
            self.move_file(file_name, dest_path_documents)
        elif ext in image_extensions:
            self.move_file(file_name, dest_path_images)
        elif ext in sound_extensions:
            self.move_file(file_name, dest_path_sounds)
        elif ext in video_extensions:
            self.move_file(file_name, dest_path_videos)
        else:
            self.move_file(file_name, dest_path_miscellaneous)

    # if a file exists in the dest dir then make the new file unique 
    def make_unique(self, file_name, dest_folder):
        name, extension = os.path.splitext(file_name)
        unique_name = file_name
        count = 1

        while(os.path.exists(os.path.join(dest_folder, unique_name))):
            unique_name = f"{name}{(count)}{extension}" # modify the file name so that it had a unique number until the file name is unique
            count += 1

        return unique_name    
   

    def move_file(self, file_name, dest_folder):
        fName = self.make_unique(file_name, dest_folder)
        source_path = os.path.join(user_dir_path, file_name)
        dest_path = os.path.join(dest_folder, fName)

        shutil.move(source_path, dest_path)
        self.print_file(file_name, dest_folder)

    
    def print_file(self, file_name, dest_folder):
        print(f"File: {os.path.basename(file_name).ljust(30)} | Moved to: {dest_folder}")

    def print_start(self):
        print("Starting cleanup...")
        print("=" * 120)

    def print_end(self):
        print("=" * 120)
        print("Cleanup finished")

# Watchdog quickstart code from 
# https://pythonhosted.org/watchdog/quickstart.html

if __name__ == "__main__": # ensures that the script will only exectue when directly ran not if it is imported as a module
    # formats the log
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    user_dir_path= input("Enter a folder you would like to be cleaned: ")
    event_handler = customEventHandler()
    event_handler.clean_folder()
    observer = Observer()
    observer.schedule(event_handler, user_dir_path, recursive=True) # observer.schedule expects a instance of FileSystemEventHandler or a subclass
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print()
        event_handler.print_end()
        observer.stop()
    observer.join()
    