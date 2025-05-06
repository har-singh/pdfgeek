import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QSpinBox, QLabel
from PyPDF2 import PdfReader, PdfWriter

class PDFSplitter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Splitter")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Select page to extract:")
        self.layout.addWidget(self.label)

        self.page_spin = QSpinBox()
        self.page_spin.setMinimum(1)
        self.layout.addWidget(self.page_spin)

        self.upload_btn = QPushButton("Upload PDF")
        self.upload_btn.clicked.connect(self.upload_pdf)
        self.layout.addWidget(self.upload_btn)

        self.extract_btn = QPushButton("Extract Page")
        self.extract_btn.clicked.connect(self.extract_page)
        self.layout.addWidget(self.extract_btn)

        self.pdf_path = None
        self.reader = None

        self.page_icons_label = QLabel("Pages:")
        self.layout.addWidget(self.page_icons_label)


    def upload_pdf(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if file_name:
            self.pdf_path = file_name
            self.reader = PdfReader(file_name)
            num_pages = len(self.reader.pages)
            self.page_spin.setMaximum(num_pages)
            self.page_icons_label.setText("Pages: " + "📄 " * num_pages)


    def extract_page(self):
        if not self.reader:
            return
        page_num = self.page_spin.value() - 1
        writer = PdfWriter()
        writer.add_page(self.reader.pages[page_num])
        out_path, _ = QFileDialog.getSaveFileName(self, "Save Extracted Page", "", "PDF Files (*.pdf)")
        if out_path:
            with open(out_path, "wb") as f:
                writer.write(f)

app = QApplication(sys.argv)
window = PDFSplitter()
window.show()
sys.exit(app.exec_())
