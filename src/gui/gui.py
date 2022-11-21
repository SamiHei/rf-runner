import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import time

from src.test_reader.test_reader import TestReader
from src.server.server import start_server


class Gui(tk.Tk):


    def __init__(self):
        super().__init__()
        self.tr = TestReader()
        self.selected_file = None
        self.application_title = "RF Runner"
        self.button_padding = "5 5 5 5"
        self.window_size = "600x800"


    def start_application(self):
        self.mainloop()


    def create_gui(self):
        self.geometry(self.window_size)
        self.minsize(600, 800)
        self.maxsize(600, 800)
        self.title(self.application_title)

        # Frames are from top to bottom first, second etc.
        first_frame = tk.Frame(self)
        first_frame.grid(row=0, column=0)

        second_frame = tk.Frame(self)
        second_frame.grid(row=1, column=0)

        third_frame = tk.Frame(self)
        third_frame.grid(row=2, column=0)

        fourth_frame = tk.Frame(self)
        fourth_frame.grid(row=3, column=0)

        # First frame block
        lb_sb = ttk.Scrollbar(first_frame,orient="vertical")
        lb_sb.grid(column=1, row=0, sticky='ns')

        list_box = tk.Listbox(first_frame, width=65, height=30, selectmode="multiple")
        list_box.grid(column=0, row=0, padx=(35,0), pady=5)
        list_box.config(yscrollcommand= lb_sb.set, exportselection=False)

        lb_sb.config(command = list_box.yview)

        # Second frame button row
        ttk.Button(second_frame,
                   text="File",
                   padding=self.button_padding,
                   command=lambda : self.write_tests_to_lb(list_box)
        ).grid(column=0, row=0, padx=5)

        ttk.Button(second_frame,
                   text="Select All",
                   padding=self.button_padding,
                   command=lambda : list_box.select_set(0, tk.END)
        ).grid(column=1, row=0, padx=5)

        ttk.Button(second_frame,
                   text="Clear Selection",
                   padding=self.button_padding,
                   command=lambda : list_box.selection_clear(0, tk.END)
        ).grid(column=2, row=0, padx=5)

        # Third frame block
        tk.Label(third_frame,text="Report target folder").grid(column=0, row=0, padx=(0, 27.5), pady=(15, 0))
        target_folder_text = tk.StringVar()
        target_folder_entry = ttk.Entry(third_frame, textvariable=target_folder_text).grid(column=0, row=1, padx=25)

        rand = tk.IntVar()
        tk.Checkbutton(third_frame, text="Randomize test order", variable=rand).grid(column=0, row=2, padx=(0, 15))
        ttk.Button(third_frame,
                   text="Run",
                   padding=self.button_padding,
                   command=lambda : self.run_tests(list_box, self.selected_file, target_folder_text.get(), rand.get())
        ).grid(column=1, row=1, padx=25)

        # Fourth frame block
        ttk.Button(fourth_frame,
                   text="Reports",
                   padding=self.button_padding,
                   command=lambda : start_server()
        ).grid(column=0, row=0, padx=(0,50), pady=(50,0))

        ttk.Button(fourth_frame,
                   text="Quit",
                   padding=self.button_padding,
                   command=self.destroy
        ).grid(column=1, row=0, padx=(80,0), pady=(50,0))


    def write_tests_to_lb(self, list_box):
        """
        Writes test cases that are read from selected file
        to given list box element
        """
        self.selected_file = filedialog.askopenfilename()

        if (self.selected_file):

            test_cases = self.tr.read_tests(self.selected_file)

            for case in test_cases:
                list_box.insert(tk.END, case)


    def run_tests(self, list_box, test_file, target_folder, rand):
        """
        Get selected cases from list box and create a robot command
        that is called via os.system call
        """
        selections = list_box.curselection()
        cases = []

        for s in selections:
            cases.append(list_box.get(s))

        if (not test_file):
            print("Test file is not selected!")
        elif (not cases):
            print("Test cases are not selected!")
        else:
            command = self.tr.create_robot_command(cases, test_file, target_folder, rand)

            print(command)
            os.system(command)

