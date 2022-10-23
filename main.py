#!/usr/bin/python3

from src.test_reader.test_reader import TestReader
import os

def main():
    t = TestReader()
    test_file = "example.robot"
    t.read_tests(test_file)

    command_string = "robot -d results"

    for test in t.tests:
        command_string += " -t " + "\"" + test + "\""

    command_string += " " + test_file

    os.system(command_string)


if __name__ == '__main__':
    main()
