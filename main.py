import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk


class FantasyCalendarApp:

    def __init__(self):
        self.main_window = ThemedTk(theme="black")
        self.configure_main_window()

        self.current_calendar = ""

        self.top_menu_frame = ttk.Frame(self.main_window, height=30)
        self.top_menu_frame.pack(padx=10, pady=10, fill=X)

        self.main_menu = Menu(self.main_window)

        self.bottom_menu_frame = ttk.Frame(self.main_window, height=30)
        self.bottom_menu_frame.pack(padx=10, pady=10, fill=X, anchor=S)

        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.configure_file_menu()

        self.main_window.mainloop()

    def configure_main_window(self):
        """
        Main window configuration. Size, position and background colour.
        """
        self.main_window.title("Fantasy Calendar")
        self.main_window.resizable(TRUE, TRUE)
        rectangle_geometry = self.create_geometry_for_center(self.main_window.winfo_screenwidth(),
                                                             self.main_window.winfo_screenheight())
        self.main_window.geometry(rectangle_geometry)
        self.main_window.config(bg="#444444")

    def configure_file_menu(self):
        """
        File menu command entries.
        """
        self.file_menu.add_command(label="New Calendar...", underline=0, command=self.create_new_calendar)
        self.file_menu.add_command(label="Save Calendar", underline=0, command=NONE)
        self.file_menu.add_command(label="Save Calendar As...", underline=14, command=NONE)
        self.file_menu.add_command(label="Import Calendar...", underline=0, command=NONE)
        self.file_menu.add_command(label="Open...", underline=0, command=NONE)
        self.file_menu.add_command(label="Exit", underline=1, command=self.main_menu.quit)

        self.main_menu.add_cascade(label="File", underline=0, menu=self.file_menu)
        self.main_window.config(menu=self.main_menu)

    @staticmethod
    def number_to_string(number):
        """
        Transform a given number in string removing '.0' ending.
        :param number: A number to have its ending fixed and transformed to string.
        :return: The given number without '.0' ending transformed into string.
        """
        return str(('%f' % number).rstrip('0').rstrip('.'))

    def create_geometry_for_center(self, width, height):
        """
        Create a rectangle geometry used to create windows and position them in center of screen.
        :param width: Width of the desired window.
        :param height: Height of the desired window.
        :return: A string containing size and position for the desired window.
        """
        position_x = self.number_to_string((self.main_window.winfo_screenwidth() - width)/2)
        position_y = self.number_to_string((self.main_window.winfo_screenheight() - height)/2)
        return self.number_to_string(width) + "x" + self.number_to_string(height) + "+" + position_x + "+" + position_y

    def create_new_calendar(self):
        """
        Creates a centered window with options to create a new calendar.
        """
        window = Toplevel()
        window.title("New Calendar")
        window.resizable(FALSE, FALSE)
        window.geometry(self.create_geometry_for_center(480, 320))
        Label(window, text="Something", pady=30, font="Comic 12").pack(expand=YES)
        Button(window, text="Create", command=window.destroy).pack(pady=30)

    def save_calendar(self):
        """
        Saves current working calendar.
        """
        files = [  # ('All Files', '*.*'),
                 ('Fantasy Calendar File', '*.fcf'),
                 ('Comma Separated File', '*.csv')]
        self.current_calendar = tkinter.filedialog.asksaveasfilename(filetypes=files)

    def send_message(self, message_type, text_message, button_message):
        """
        Creates a centered window with custom message.
        :param message_type: Window name.
        :param text_message: Text to be displayed in window body.
        :param button_message: Close button text.
        """
        window = Toplevel()
        window.title(message_type)
        window.resizable(FALSE, FALSE)
        window.geometry(self.create_geometry_for_center(300, 200))
        Label(window, text=text_message, pady=30, font="Comic 12").pack(expand=YES)
        Button(window, text=button_message, command=window.destroy).pack(pady=30)


FantasyCalendarApp()
