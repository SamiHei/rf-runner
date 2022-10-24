from tkinter import *
from tkinter import ttk

class Gui:

    def __init__(self, x, y):
        self.root = None


    def create_gui(self):
        self.root = Tk()
        self.root.geometry("1200x700")
        self.root.title("RF Runner")

        frame = ttk.Frame(self.root, padding=10)
        frame.grid()

        ttk.Button(frame, text="Quit", command=self.root.destroy).grid(column=0, row=0)


    def start_gui(self):
        self.root.mainloop()
