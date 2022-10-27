import re

class TestReader:

    def __init__(self):
        pass


    def read_tests(self, file):
        """
        Goes through the test case file and collects all the test case names
        under *** Test Cases ***
        """
        tests = []
        
        with open(file, "r") as f:
            # Set pointer to start of *** Test Cases *** block
            for line in f:
                if (line.strip() == "*** Test Cases ***"):
                    break

            # Loop through lines and exlude if starting 4 spaces or tab
            for line in f:
                
                if not(re.match("    .*", line) or re.match("\t.*", line) or (line == "") or (line == "\n")):
                    tests.append(line.strip())

        return tests


