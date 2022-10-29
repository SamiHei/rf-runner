import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
from src.test_reader.test_reader import TestReader


class Gui(tk.Tk):

    def __init__(self):
        super().__init__()
        self.tr = TestReader()
        self.selected_file = None


    def create_gui(self):
        self.geometry("400x700")
        self.title("RF Runner")

        list_box = tk.Listbox(self, selectmode="multiple")

        list_box.grid(row=1)

        button1 = ttk.Button(self, text="Quit", padding="10 10 10 10", command=self.destroy).grid(column=0, row=0)
        button2 = ttk.Button(self, text="Run", padding="10 10 10 10", command=lambda : self.run_tests(list_box, self.selected_file)).grid(column=1, row=0)
        button3 = ttk.Button(self, text="File", padding="10 10 10 10", command=lambda : self.write_list_box_content(list_box)).grid(column=2, row=0)


    def start_gui(self):
        self.mainloop()


    def write_list_box_content(self, list_box):

        self.selected_file = filedialog.askopenfilename()

        test_cases = self.tr.read_tests(self.selected_file)

        for case in test_cases:
            list_box.insert(tk.END, case)


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

