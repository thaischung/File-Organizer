````markdown
# File Organizer

A Python program that cleans and organizes a user-specified directory by automatically sorting files into separate folders based on their file extensions.

Files are organized into categories such as:

- Documents
- Images
- Audio
- Videos
- Miscellaneous files

The program uses the `watchdog` Python module to monitor the selected directory for new files.

---

## Requirements

Before running the program, make sure you have:

- Python 3
- pip
- `watchdog`

You can check whether Python is installed with:

```bash
python3 --version
```

On Windows:

```bash
python --version
```

You can check whether pip is installed with:

```bash
pip --version
```

---

## Windows Installation

### 1. Download the Project

Download `folderCleaner.py` and place it inside a folder for the project.

### 2. Configure the Directories

Open `folderCleaner.py` and enter the directory paths you want the program to monitor and use for organized files.

### 3. Install Python

If Python is not already installed, download and install Python 3.

Check your installation with:

```bash
python --version
```

### 4. Check pip

pip is normally included with modern Python installations.

Check that it is installed with:

```bash
pip --version
```

### 5. Navigate to the Project Directory

Open Command Prompt or PowerShell and navigate to the folder containing the program:

```bash
cd path\to\your\folder
```

### 6. Create a Virtual Environment

```bash
python -m venv venv
```

### 7. Activate the Virtual Environment

#### Command Prompt

```bash
venv\Scripts\activate
```

#### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### 8. Install Watchdog

```bash
pip install watchdog
```

### 9. Run the Program

```bash
python folderCleaner.py
```

To stop the program, press:

```text
Ctrl + C
```

---

## macOS / Linux Installation

### 1. Download the Project

Download `folderCleaner.py`.

### 2. Create a Project Folder

Create a folder for the program and move `folderCleaner.py` into it.

### 3. Configure the Directories

Open `folderCleaner.py` and enter the directory paths you want the program to monitor and use for organized files.

### 4. Check Python

Make sure Python 3 is installed:

```bash
python3 --version
```

### 5. Check pip

Check whether pip is installed:

```bash
python3 -m pip --version
```

If pip is not installed, install it using the appropriate method for your operating system.

### 6. Navigate to the Project Directory

Check your current directory with:

```bash
pwd
```

Then navigate to the folder containing the program:

```bash
cd /path/to/your/folder
```

### 7. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 8. Activate the Virtual Environment

```bash
source venv/bin/activate
```

You should now see `(venv)` at the beginning of your terminal prompt.

### 9. Install Watchdog

```bash
pip install watchdog
```

### 10. Run the Program

```bash
python3 folderCleaner.py
```

To stop the program, press:

```text
Ctrl + C
```

---

## Running the Program Again

After the initial setup, you do **not** need to recreate the virtual environment or reinstall `watchdog`.

Navigate to the project directory:

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

## Stopping the Program

The program continuously monitors the selected directory while it is running.

To stop it at any time, press:

```text
Ctrl + C
```
````
