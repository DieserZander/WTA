from tkinter import *


class MainWindow():
    def __init__(self):
        self.root = Tk()
        self.root.minsize(150, 160)
        self.root.title("WTA")

        self.setup_window()

    def update_window(self):
        pass

    def setup_window(self):
        self.root.mainloop()
