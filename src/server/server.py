from flask import Flask, render_template
import os


app = Flask(__name__)

BASE_REPORTS_PATH = ""


def main():
    app.run()


@app.route('/')
def index():
    reports_options = get_reports_folder_path()
    return render_template('index.html', options=reports_options)


def get_reports_folder_path():
    """
    Create dictionary with absolute path for each reports file
    and reports folder name to be shown in the dropdown menu
    """

    reports_path_dict = []

    for folder in os.listdir(BASE_REPORTS_PATH):
        path = BASE_REPORTS_PATH + "/" + folder + "/log.html"
        option_dict = { "path": path,
                        "folder": folder
                      }
        reports_path_dict.append(option_dict)

    return reports_path_dict


if __name__=='__main__':
    main()

