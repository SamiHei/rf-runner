#!/usr/bin/python3

from src.test_reader.test_reader import TestReader
from src.gui.gui import Gui
import os


if __name__ == '__main__':
    g = Gui()
    g.create_gui()
    g.start_application()

