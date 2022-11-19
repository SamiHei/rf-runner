from flask import Flask, render_template
import os


reports_folder = 'test_results'

app = Flask(__name__,
            static_folder=reports_folder)


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
    base_reports_path = os.getcwd() + f'/{reports_folder}'

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


if __name__=='__main__':
    main()

