#!/usr/bin/python3

from src.test_reader.test_reader import TestReader
from src.gui.gui import Gui
import os


def main():
    g = Gui()
    g.create_gui()
    g.start_application()


if __name__ == '__main__':
    main()

