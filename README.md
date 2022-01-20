# Positron - Editor

A basic text editor written in Python with the PyQt6 framework.
Forms part of the Positron Software Suite.

## Structure

### Source Code Files

- `MainWindow.py` - Main Application File

- `UI_MainWindow.py` - Qt-Designer File Converted to Python

- `UI_MainWindow.ui` - QT-Designer File

### Python Package Files

- `Pipfile`
- `Pipfile.lock`
- `requirements.txt`

### PyInstaller Files

- `/build`
- `/dist`
- `MainWindow.spec`

## Build Instructions

### To Modify Project

- If required open `UI_MainWindow.ui` file in Qt-Designer and modify layout
- Run `pyuic6 -x UI_MainWindow.ui -o UI_MainWindow.py` to convert `.ui` to Python

### To Debug

- Run `python3 MainWindow.py` to launch application to debug

### To Build

- Update software version in `.spec` file
- Update software version in `.ui` file via QtDesigner Software
- Run `pipenv run python3 freeze > requirements.txt`
- Run `pyinstaller --onefile MainWindow.py` to compile project to single executable file
