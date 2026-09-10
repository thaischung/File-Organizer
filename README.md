# FileDaemon

FileDaemon is a Python file organizer that cleans and monitors a user-selected directory.

Files are automatically sorted into folders based on their file extension:

* **Documents**
* **Images**
* **Audios**
* **Videos**
* **Miscellaneous**

FileDaemon uses Python's [`watchdog`](https://pypi.org/project/watchdog/) library to monitor the selected directory for newly created files and organize them automatically.

## Features

* Organizes existing files in a directory
* Monitors the directory for newly created files
* Automatically categorizes files by extension
* Prevents duplicate filenames by renaming conflicting files
* Supports custom source and destination directories
* Saves previous directory settings for future runs
* Supports Windows, macOS, and Linux

---

## Requirements

You need:

* Python 3
* Git

All required Python packages are installed automatically from `requirements.txt`.

---

# macOS / Linux

## 1. Clone the Repository

```bash
git clone <repository-url>
cd FileDaemon
```

## 2. Make the Launcher Executable

The first time you run FileDaemon, give the launcher execute permission:

```bash
chmod +x run.sh
```

## 3. Run FileDaemon

```bash
./run.sh
```

The launcher will automatically:

1. Create a Python virtual environment if one does not already exist
2. Install the packages listed in `requirements.txt`
3. Start FileDaemon

You do not need to manually activate the virtual environment.

---

# Windows

## 1. Clone the Repository

Open Command Prompt or PowerShell:

```powershell
git clone <repository-url>
cd FileDaemon
```

## 2. Create a Virtual Environment

```powershell
python -m venv venv
```

## 3. Activate the Virtual Environment

### Command Prompt

```cmd
venv\Scripts\activate
```

### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

## 4. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

## 5. Run FileDaemon

```powershell
python folderCleaner.py
```

---

# First Run

When FileDaemon is started for the first time, it will ask for two directories.

```text
Saved Settings Not Found.

Enter your source directory:
> ~/Downloads

Enter your destination directory:
> ~/Downloads
```

The **source directory** is the directory FileDaemon monitors and cleans.

The **destination directory** is where FileDaemon creates its organization folders:

```text
Destination/
├── Documents/
├── Images/
├── Audios/
├── Videos/
└── Miscellaneous/
```

After configuration, FileDaemon will clean existing files and begin monitoring the source directory for new files.

---

# Saved Settings

FileDaemon remembers the source and destination directories from the previous run.

The next time the program starts, it will display the saved settings:

```text
Saved Settings Found.

Source Folder To Clean: /home/user/Downloads
Destination Folder: /home/user/Downloads

Would You Like To Use These Settings? [Y/N]
```

Enter:

```text
Y
```

to use the previous settings.

Enter:

```text
N
```

to enter new source and destination directories.

---

# Stopping FileDaemon

FileDaemon continues monitoring the source directory until it is stopped.

Press:

```text
Ctrl + C
```

to exit the program.

---

# Running FileDaemon Again

### macOS / Linux

Simply run:

```bash
./run.sh
```

The existing virtual environment will automatically be reused.

### Windows

Activate the existing virtual environment:

```powershell
venv\Scripts\activate
```

Then run:

```powershell
python folderCleaner.py
```

---

# Project Structure

```text
FileDaemon/
├── folderCleaner.py
├── requirements.txt
├── run.sh
├── configs.json
├── README.md
└── .gitignore
```

`venv/` is created locally when the program is set up and should not be committed to Git.

---

# Dependencies

Python dependencies are stored in `requirements.txt`.

Currently:

```text
watchdog==6.0.0
```

To install them manually:

```bash
python3 -m pip install -r requirements.txt
```

---

# License

This project is intended for educational and personal use.
