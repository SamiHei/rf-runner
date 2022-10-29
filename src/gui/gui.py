import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import time

from src.test_reader.test_reader import TestReader


class Gui(tk.Tk):

    def __init__(self):
        super().__init__()
        self.tr = TestReader()
        self.selected_file = None


    def start_application(self):
        self.mainloop()


    def create_gui(self):
        self.geometry("400x700")
        self.title("RF Runner")

        list_box = tk.Listbox(self, selectmode="multiple")
        list_box.grid(row=1)

        button1 = ttk.Button(self, text="File", padding="10 10 10 10", command=lambda : self.write_tests_to_lb(list_box)).grid(column=0, row=0)

        button2 = ttk.Button(self, text="Quit", padding="10 10 10 10", command=self.destroy).grid(column=0, row=2)
        button3 = ttk.Button(self, text="Run", padding="10 10 10 10", command=lambda : self.run_tests(list_box, self.selected_file)).grid(column=1, row=2)


    def write_tests_to_lb(self, list_box):
        """
        Writes test cases that are read from selected file
        to given list box element
        """
        try:
            self.selected_file = filedialog.askopenfilename()

            test_cases = self.tr.read_tests(self.selected_file)

            for case in test_cases:
                list_box.insert(tk.END, case)
        except TypeError:
            # Handler if you close the filedialog without selecting file
            pass


    def run_tests(self, list_box, test_file):
        """
        Get selected cases from list box and create a robot command
        that is called via os.system call
        """
        try:
            selections = list_box.curselection()
            cases = []

            for s in selections:
                cases.append(list_box.get(s))

            command = self.tr.create_robot_command(cases, test_file)

            print(command)
            os.system(command)
        except TypeError:
            print("File not selected!")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
