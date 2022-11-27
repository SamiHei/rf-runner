from flask import Flask, render_template
import os
import threading
import logging

from src.configs.configs import ConfigsHandler


ch = ConfigsHandler()
reports_folder = ch['reports']['REPORTS_FOLDER']

# For some reason static_folder must be set here and can't be set
# before starting the app so need to init ConfigHandler here and fetch config
app = Flask(__name__,
            static_folder=reports_folder)


def start_server(host, port):
    """
    Creates Flask web server on a thread and sets logging to level ERROR

    Params:
     host : string Host IP from config.ini fil
     port : string Port number from config.ini file
    """
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    thread = threading.Thread(target=lambda : app.run(host=host, port=port))
    thread.daemon = True
    thread.start()
    print(f'Server started at: http://{host}:{port}')


@app.route('/')
def index():
    reports_options = __get_reports_folder_path()
    return render_template('index.html', options=reports_options)


def __get_reports_folder_path():
    """
    Create dictionary with absolute path for each reports file
    and reports folder name to be shown in the dropdown menu
    """
    reports_path_dict = []
    base_reports_path = os.getcwd() + f'/src/server/{reports_folder}'

    try:
        for folder in os.listdir(base_reports_path):
            path = f'/{reports_folder}' + "/" + folder + "/log.html"
            option_dict = { "path": path,
                            "folder": folder
            }
            reports_path_dict.append(option_dict)

        return reports_path_dict
    except FileNotFoundError:
        # If no test has been run yet so reports_folder does not exists
        return []

