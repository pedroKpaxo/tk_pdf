from tkinter import messagebox, ttk
from tkinter import filedialog, scrolledtext, Tk, Menu

from abc import ABC


class BaseTkApp(ABC):
    """
    A base class for creating Tkinter applications.
    It provides methods for displaying file and folder dialogs, and messages.
    """

    def __init__(self):
        self.root = Tk()
        self.root.title("PDF Viewer")
        self.root.geometry("500x500")
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

    def run(self):
        """
        Runs the application.
        This method should be called after all the widgets have been created.
        """
        self.root.mainloop()

    def display_filedialog(self):
        """
        Displays a file dialog and returns the path of the selected file.
        If no file is selected, returns None.
        Returns:
            str: A string containing the path of the selected file.
        """
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            return file_path
        return None

    def display_save_dialog(self):
        """
        Displays a save dialog and returns the path of the selected file.
        If no file is selected, returns None.
        Returns:
            str: A string containing the path of the selected file.
        """
        file_path = filedialog.asksaveasfilename(
            filetypes=[("Text Files", "*.txt")])
        if file_path:
            return file_path
        return None

    def display_foledialog(self):
        """
        Displays a folder dialog and returns the path of the selected folder.
        If no folder is selected, returns None.
        Returns:
            str: A string containing the path of the selected folder.
        """
        folder_path = filedialog.askdirectory()
        if folder_path:
            return folder_path
        return None

    def display_message(self, message):
        """
        Displays a message box with the given message.
        Args:
            message (str): The message to display.
        """
        messagebox.showinfo("Message", message)

    def display_error(self, message):
        """
        Displays an error message box with the given message.
        Args:
            message (str): The message to display.
        """
        messagebox.showerror("Error", message)


class PDFViewer(BaseTkApp):
    def __init__(self):
        super().__init__()
        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        self.file_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(menu=self.file_menu, label="File")

    def create_widgets(self):
        self.open_button = ttk.Button(self.root, text="Open PDF")
        self.open_button.pack()

        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, fill='both')

        # Create a ScrolledText widget (which includes a scroll bar)
        self.text_area = scrolledtext.ScrolledText(self.frame, wrap='word')
        self.text_area.pack(expand=True, fill='both')
