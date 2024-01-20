from PyPDF2 import PdfReader

from .view import PDFViewer
from typing import TypedDict


class MenuCommand(TypedDict):
    label: str
    command: callable


class AppController:

    def __init__(self):
        self.view = PDFViewer()
        self.view.open_button.config(command=self.open_pdf)

    @property
    def commands(self) -> list[MenuCommand]:
        return [
            {"label": "Open PDF", "command": self.open_pdf},
            {"label": "Save PDF as TXT", "command": self.save_pdf_txt},
        ]

    def create_file_commands(self):
        for command in self.commands:
            self.view.file_menu.add_command(label=command["label"], command=command["command"])  # noqa
        self.view.file_menu.add_separator()
        self.view.file_menu.add_command(label="Exit", command=self.view.root.quit)  # noqa

    def run(self):
        """
        Runs the application.
        This method should be called after all the widgets have been created.
        """
        self.create_file_commands()
        self.view.run()

    def open_pdf(self):
        file_path = self.view.display_filedialog()
        if file_path:
            try:
                pdf = PdfReader(file_path)
                self.display_pdf(pdf)
            except Exception as e:
                self.view.display_error(str(e))

    def display_pdf(self, pdf: PdfReader):
        self.view.text_area.config(state='normal')
        self.view.text_area.delete(1.0, 'end')
        for page in pdf.pages:
            text = page.extract_text()
            self.view.text_area.insert('end', text)
        self.view.text_area.config(state='disabled')
        self.get_view_text()

    def get_view_text(self):
        """
        Gets the text from the view.
        Returns:
            str: The text from the view.
        """
        # Check if the text area has text.
        if not self.view.text_area.get("1.0", "end-1c"):
            self.view.display_error("No text to copy.")
            return
        return self.view.text_area.get("1.0", "end-1c")

    def save_pdf_txt(self):
        """
        Saves the text from the view to a text file.
        """
        text = self.get_view_text()

        if not text:
            return
        file_path = self.view.display_save_dialog() + ".txt"
        if not file_path:
            return
        try:
            with open(file_path, "w") as f:
                f.write(text)
        except Exception as e:
            self.view.display_error(str(e))
            return
