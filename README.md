# PDF Splitter GUI

Prompt to ChatGPT

First prompt:

> I want to create a simple windows application with gui where pdf document is uploaded and I can split or extract the pages

Second prompt:

> I have python code to split the pdf document. It is very basic. Now I want that once uploaded it actually show the page representations. representations could be simple emoji so if there are thee pages there are three page icons

In order to generate the executable file a Windows 11 pro virtual machine was created in Azure. On the vm python was installed using `winget install Python.Python.3.12`.

Here the commands that were used to create the executable files.

```powershell
# Optional: Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install pyinstaller PyQt5 PyPDF2

# Package your script
pyinstaller --onefile --windowed pdfgeek.py
```

Third prompt:

Very good. Not how to make it the icon selectable? Use can select the icons and then extract the page. the output is the document with selected pages (icons)
