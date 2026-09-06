# File Organizer

This program cleans out a user-specified directory and organizes different file types into separate folders based on their file extensions.

Files are organized into categories such as:

- Documents
- Images
- Audio
- Videos
- Miscellaneous

The program uses the Python `watchdog` module to monitor the selected directory for new files.

---

## Requirements

Before running the program, make sure you have:

- Python 3
- pip
- watchdog

---

# Windows Setup

## 1. Download the Python File

Download `folderCleaner.py` and place it inside a folder.

## 2. Configure the Paths

Open `folderCleaner.py` and fill in the directory paths at the top of the file.

## 3. Install Python

Download Python if it is not already installed.

You can check whether Python is installed with:

```bash
python --version
```

## 4. Check pip

pip is normally installed automatically with Python.

Check whether pip is installed with:

```bash
pip --version
```

## 5. Navigate to the Project Folder

Open **Command Prompt** or **PowerShell** and navigate to the folder containing `folderCleaner.py`.

```bash
cd path\to\your\folder
```

## 6. Create a Virtual Environment

```bash
python -m venv venv
```

## 7. Activate the Virtual Environment

### Command Prompt

```bash
venv\Scripts\activate
```

### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

## 8. Install Watchdog

```bash
pip install watchdog
```

## 9. Run the Program

```bash
python folderCleaner.py
```

To stop the program, press:

```text
Ctrl + C
```

---

# macOS / Linux Setup

## 1. Download the Python File

Download `folderCleaner.py`.

## 2. Create a Project Folder

Create a folder for the Python file and move `folderCleaner.py` into it.

## 3. Configure the Paths

Open `folderCleaner.py` and fill in the directory paths at the top of the file.

## 4. Check Python

Make sure Python 3 is installed:

```bash
python3 --version
```

## 5. Check pip

Check whether pip is installed:

```bash
python3 -m pip --version
```

## 6. Navigate to the Project Folder

Check your current directory with:

```bash
pwd
```

Navigate to the folder containing `folderCleaner.py`:

```bash
cd /path/to/your/folder
```

## 7. Create a Virtual Environment

```bash
python3 -m venv venv
```

## 8. Activate the Virtual Environment

```bash
source venv/bin/activate
```

After activation, you should see `(venv)` at the beginning of your terminal prompt.

## 9. Install Watchdog

```bash
pip install watchdog
```

## 10. Run the Program

```bash
python3 folderCleaner.py
```

To stop the program, press:

```text
Ctrl + C
```

---

# Running the Program Again

After completing the initial setup, you do **not** need to recreate the virtual environment or reinstall `watchdog`.

Navigate to your project folder:

```bash
cd /path/to/your/folder
```

Activate the virtual environment.

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Then run the program.

### macOS / Linux

```bash
python3 folderCleaner.py
```

### Windows

```bash
python folderCleaner.py
```

---

# Stopping the Program

The program continuously monitors the selected directory while it is running.

To stop the program:

```text
Ctrl + C
```
