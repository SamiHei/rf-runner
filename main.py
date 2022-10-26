#!/usr/bin/python3

from src.test_reader.test_reader import TestReader
from src.gui.gui import Gui
import os

def main():
    t = TestReader()
    test_file = "example.robot"
    t.read_tests(test_file)

    # command_string = "robot -d results"

    # i = 0
    # for test in t.tests:
    #     if (i%2 != 0):
    #         command_string += " -t " + "\"" + test + "\""
    #     i += 1

    # command_string += " " + test_file

    g = Gui(100, 500)
    g.create_gui(t.tests, test_file)
    g.start_gui()


if __name__ == '__main__':
    main()
