# PDF Splitter GUI

A minimal Windows GUI app to upload, preview, and split PDF documents. Built from scratch using Python and packaged into an executable in under 2 hours.

## Features

- Upload a PDF.
- Display pages as icons (📄).
- Select pages via icons.
- Extract selected pages into a new PDF.

## Background

Frustrated by the dependency hell of old tools like PDFsam (Java required), this project was built as a clean, native alternative using Python and ChatGPT prompts. Full write-up: [Created First Ever Windows Executable Software in 2 Hours](https://blog.geekfive.co.uk/blog/2025/05/06/windows-pdf-exe.html)

## Tech Stack

- **Python 3.12**
- **PyQt5** — GUI
- **PyPDF2** — PDF handling
- **PyInstaller** — Build `.exe`

## Build Instructions

Tested on Windows 11 Pro VM (Azure). Install Python via:

```powershell
winget install Python.Python.3.12
````

### Steps

```powershell
# (Optional) Set up a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install pyinstaller PyQt5 PyPDF2

# Package into executable
pyinstaller --onefile --windowed pdfgeek.py
```

## Usage

1. Run the app (`.exe`).
2. Upload a PDF file.
3. Page icons appear (📄).
4. Click icons to select pages.
5. Click "Extract" to save a new PDF with selected pages.

## Notes

* Clean, no-frills UI.
* Emoji icons represent pages.
* Output PDF is saved in the same folder as the original.
* Built fast, works fast.
