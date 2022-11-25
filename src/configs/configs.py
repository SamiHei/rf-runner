import configparser

class ConfigsHandler(configparser.ConfigParser):


    def __init__(self):
        super().__init__()
        self.config_file = 'config.ini'
        self.read(self.config_file)

