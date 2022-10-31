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
        self.application_title = "RF Runner"
        self.button_padding = "10 10 10 10"
        self.window_size = "400x700"


    def start_application(self):
        self.mainloop()


    def create_gui(self):
        self.geometry(self.window_size)
        self.title(self.application_title)

        list_box = tk.Listbox(self, selectmode="multiple")
        list_box.grid(row=1)

        button1 = ttk.Button(self, text="File", padding=self.button_padding, command=lambda : self.write_tests_to_lb(list_box)).grid(column=0, row=0)

        button2 = ttk.Button(self, text="Quit", padding=self.button_padding, command=self.destroy).grid(column=0, row=2)
        button3 = ttk.Button(self, text="Run", padding=self.button_padding, command=lambda : self.run_tests(list_box, self.selected_file, target_folder_text.get(), rand.get())).grid(column=1, row=2)

        target_folder_label = tk.Label(self, text="Report target folder").grid(column=0, row=3)
        target_folder_text = tk.StringVar()
        target_folder_entry = ttk.Entry(self, textvariable=target_folder_text).grid(column=0, row=4)

        rand = tk.IntVar()
        randomize = tk.Checkbutton(self, text="Randomize test order", variable=rand).grid(column=0, row=5)


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


    def run_tests(self, list_box, test_file, target_folder, rand):
        """
        Get selected cases from list box and create a robot command
        that is called via os.system call
        """
        try:
            selections = list_box.curselection()
            cases = []

            for s in selections:
                cases.append(list_box.get(s))

            command = self.tr.create_robot_command(cases, test_file, target_folder, rand)

            print(command)
            os.system(command)
        except TypeError:
            print("File not selected!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

