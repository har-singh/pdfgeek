# PDF Splitter GUI

A simple Windows GUI application to upload, preview, and split PDF documents.

## Features

- Upload a PDF document.
- Visualize pages using basic icons (e.g. 📄📄📄).
- Select page icons to extract.
- Generate a new PDF with selected pages.

## Tech Stack

- **Python 3.12**
- **PyQt5** — GUI
- **PyPDF2** — PDF manipulation
- **PyInstaller** — Packaging into Windows executable

## Build Instructions

Executed on a Windows 11 Pro VM (Azure). Python installed via:

```powershell
winget install Python.Python.3.12
````

### Build Steps

```powershell
# Optional: Set up virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install required packages
pip install pyinstaller PyQt5 PyPDF2

# Build executable
pyinstaller --onefile --windowed pdfgeek.py
```

## Usage

1. Launch the app.
2. Upload a PDF file.
3. Page icons appear (e.g., 📄).
4. Select desired page icons.
5. Click "Extract" — generates a new PDF with selected pages.

## Notes

* UI is minimal and functional.
* Emoji icons represent PDF pages for simplicity.
* Output is saved in the same directory as the original file.
