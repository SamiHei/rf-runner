from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os

class Gui:

    def __init__(self, x, y):
        self.root = None


    def create_gui(self, test_cases, test_file):
        self.root = Tk()
        self.root.geometry("400x700")
        self.root.title("RF Runner")

        list_box = Listbox(self.root, selectmode="multiple")

        for case in test_cases:
            list_box.insert(END, case)

        list_box.grid()

        button1 = ttk.Button(self.root, text="Quit", command=self.root.destroy).grid()
        button2 = ttk.Button(self.root, text="Run", command=lambda : self.run_tests(list_box, test_file)).grid()
        button3 = ttk.Button(self.root, text="File", command=lambda : self.select_file()).grid()


    def start_gui(self):
        self.root.mainloop()


    def run_tests(self, list_box, test_file):
        selections = list_box.curselection()
        cases = []

        for s in selections:
            cases.append(list_box.get(s))

        command_string = "robot -d results"

        for test in cases:
            command_string += " -t " + "\"" + test + "\""

        command_string += " " + test_file

        print(command_string)

        os.system(command_string)


    def select_file(self):

        file_path = filedialog.askopenfilename()

        print(file_path)

