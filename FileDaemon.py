import os
import shutil
import time
import logging
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
import json

class customEventHandler(FileSystemEventHandler): # subclass of the FileSystemEventHandler 
    def __init__(self, src_dir, dst_dir):
        self.user_source_directories = src_dir
        
        self.destinations = {
            "Documents" : os.path.join(dst_dir, "Documents"),
            "Images" : os.path.join(dst_dir, "Images"),
            "Audios" : os.path.join(dst_dir, "Audios"),
            "Videos" : os.path.join(dst_dir, "Videos"),
            "Miscellaneous" : os.path.join(dst_dir, "Miscellaneous")
        }

        self.FILE_TYPES = {
            "documents": {
                ".doc", ".docx", ".odt", ".rtf", ".txt",
                ".xls", ".xlsx", ".ods", ".csv",
                ".ppt", ".pptx", ".odp", ".pdf",
                ".epub", ".md", ".tex", ".pages"
            },

            "images": {
                ".jpeg", ".jpg", ".jfif", ".pjpeg", ".pjp",
                ".gif", ".png", ".svg", ".bmp",
                ".tiff", ".tif", ".webp", ".ico"
            },

            "audios": {
                ".mp3", ".aac", ".ogg", ".wma",
                ".m4a", ".wav", ".aiff", ".flac"
            },

            "videos": {
                ".mp4", ".mkv", ".mov", ".avi",
                ".wmv", ".flv", ".webm", ".mpeg",
                ".3gp", ".m4v"
            }
        }

        # make the directories if they do not exist on the machine already 
        for dst in self.destinations.values():
            os.makedirs(dst, exist_ok=True)
        
    def clean_folder(self): 
        self.print_start()
        with os.scandir(self.user_source_directories) as folder:
            for file in folder:
                if file.is_file():
                    # check the file types
                    file_name = file.name
                    self.check_type_and_sort(file_name)  

    def on_created(self, event):
        if event.is_directory:
            return

        file_name = os.path.basename(event.src_path)


        
        with os.scandir(self.user_source_directories) as folder:
            for file in folder:
                if file.is_file():
                    # check the file types
                    file_name = file.name
                    self.check_type_and_sort(file_name)

    def check_type_and_sort(self, file_name): 
        _, ext = os.path.splitext(file_name)
        ext = ext.lower()

        if ext in self.FILE_TYPES["documents"]:
            self.move_file(file_name, self.destinations["Documents"])
        elif ext in self.FILE_TYPES["images"]:
            self.move_file(file_name, self.destinations["Images"])
        elif ext in self.FILE_TYPES["audios"]:
            self.move_file(file_name, self.destinations["Audios"])
        elif ext in self.FILE_TYPES["videos"]:
            self.move_file(file_name, self.destinations["Videos"])
        else:
            self.move_file(file_name, self.destinations["Miscellaneous"])

    # if a file exists in the dest dir then make the new file unique 
    def make_unique(self, file_name, dest_folder):
        name, extension = os.path.splitext(file_name)
        unique_name = file_name
        count = 1

        while(os.path.exists(os.path.join(dest_folder, unique_name))):
            unique_name = f"{name} ({count}){extension}" # modify the file name so that it had a unique number until the file name is unique
            count += 1

        return unique_name    
   
    def move_file(self, file_name, dest_folder):
        fName = self.make_unique(file_name, dest_folder)
        source_path = os.path.join(self.user_source_directories, file_name)
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

def get_src_dir():
    while True:
        src = input("Enter your source directory: ").strip()

        abs_path = os.path.abspath(os.path.expanduser(src))

        if os.path.isdir(abs_path):
            return abs_path
        
        print("The path provided is not a valid path.")

def get_dest_dir():
    while True:
        dest = input("Enter your destionation directory: ").strip()

        abs_path = os.path.abspath(os.path.expanduser(dest))

        try:
            os.makedirs(abs_path, exist_ok=True)
            return abs_path
        except OSError:
            print("The path provided is not a valid path.")
        
# Watchdog quickstart code from 
# https://pythonhosted.org/watchdog/quickstart.html

if __name__ == "__main__": # ensures that the script will only exectue when directly ran not if it is imported as a module
    # formats the log
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    src = ""
    dst = ""

    try:
        with open("configs.json", "r") as file:
            configs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        configs = {}

    if not configs:
        print("Saved Settings Not Found.")
        src = get_src_dir()
        dst = get_dest_dir()
        configs['source_dir'] = src
        configs['destination_dir'] = dst

        with open("configs.json", "w") as file:
            json.dump(configs, file, indent=4)
        
    else:
        print("Saved Settings Found.")
        print(f"Source Folder To Clean: {configs['source_dir']}")
        print(f"Destination Folder: {configs['destination_dir']}")

        while True:
            answer = input(f"Would You Like To Use These Settings? [Y/N]").lower()

            if answer == "n":
                src = get_src_dir()
                dst = get_dest_dir()
                configs['source_dir'] = src
                configs['destination_dir'] = dst

                # Save the configurations
                with open("configs.json", "w") as file:
                    json.dump(configs, file, indent=4)

                break

            elif answer == "y":
                src = configs['source_dir']
                dst = configs['destination_dir']

                if not os.path.isdir(src):
                    print("Saved source directory no longer exists.")
                    src = get_src_dir()

                if not os.path.isdir(src):
                    print("Saved destination directory no longer exists.")
                    dst = get_dest_dir()

                with open("configs.json", "w") as file:
                    json.dump(configs, file, indent=4)
                
                print("Running With Saved Settings...")

                break

            else:
                print(f"ERROR: INVALID INPUT: {answer}")
     
    event_handler = customEventHandler(src, dst)
    event_handler.clean_folder()
    observer = Observer()
    observer.schedule(event_handler, src, recursive=False) # observer.schedule expects a instance of FileSystemEventHandler or a subclass
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print()
        event_handler.print_end()
        observer.stop()
    observer.join()
    