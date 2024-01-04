from tkinter import ttk
from tkinter import filedialog, scrolledtext, Tk, Menu
from PyPDF2 import PdfReader

from abc import ABC, abstractmethod


class TkApp(ABC):

    def __init__(self):
        self.root = Tk()
        self.root.title("PDF Viewer")
        self.root.geometry("500x500")
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

    def run(self):
        self.root.mainloop()

    @abstractmethod
    def create_widgets(self):
        pass


class PDFViewer(TkApp):
    def __init__(self):
        super().__init__()
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        self.file_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(menu=self.file_menu, label="File")
        self.file_menu.add_command(label="Open PDF", command=self.open_pdf)  # noqa
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

    def create_widgets(self):
        self.open_button = ttk.Button(self.root, text="Open PDF", command=self.open_pdf)  # noqa
        self.open_button.pack()

        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, fill='both')

        # Create a ScrolledText widget (which includes a scroll bar)
        self.text_area = scrolledtext.ScrolledText(self.frame, wrap='word')
        self.text_area.pack(expand=True, fill='both')

    def open_pdf(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            try:
                pdf = PdfReader(file_path)
                self.display_pdf(pdf)
            except Exception as e:
                print(e)

    def display_pdf(self, pdf: PdfReader):
        self.text_area.config(state='normal')
        self.text_area.delete(1.0, 'end')
        for page in pdf.pages:
            text = page.extract_text()
            self.text_area.insert('end', text)
        self.text_area.config(state='disabled')


if __name__ == "__main__":
    PDFViewer().run()
