import re

class TestReader:


    def __init__(self, reports_folder):
        self.reports_folder = reports_folder


    def read_tests(self, file_path):
        """
        Goes through the test case file and collects all the test case names
        under *** Test Cases ***

        Params:
         file_path : string Full path to selected .robot test file
        """
        tests = []
        
        with open(file_path, "r") as f:
            # Set pointer to start of *** Test Cases *** block
            for line in f:
                if (line.strip() == "*** Test Cases ***"):
                    break

            # Loop through lines and exlude if starting 4 spaces or tab
            for line in f:
                
                if not(re.match("    .*", line) or re.match("\t.*", line) or (line == "") or (line == "\n")):
                    tests.append(line.strip())

        return tests


    def create_robot_command(self, cases, test_file, target_folder, rand):
        """
        Wraps a robot call with test cases given to a one string

        Params:
         cases         : string[] List of test case names strings
         test_file     : string   Selected test file to be pointed on robot command
         target_folder : string   Folder name where results will be saved
         rand          : bool     Value to set if robot test cases will be ran in random order or not
        """
        command = "robot "
        results_folder_path = f"src/server/{self.reports_folder}/"

        if (rand == 1):
            command += "--randomize all "

        command += "-d " + results_folder_path + target_folder

        for test in cases:
            command += " -t " + "\"" + test + "\""

        command += " " + test_file

        return command


