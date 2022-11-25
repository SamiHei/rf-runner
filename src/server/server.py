from flask import Flask, render_template
import os
import threading
import logging

from src.configs.configs import ConfigsHandler


ch = ConfigsHandler()

# For some reason static_folder must be set here and can't be set
# before starting the app so need to init ConfigHandler here and fetch config
app = Flask(__name__,
            static_folder=ch['reports']['REPORTS_FOLDER'])


def start_server(host, port):
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

