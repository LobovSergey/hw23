import os

from flask import Flask, request, render_template

from utils import data_processing

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query/")
def perform_query():
    try:
        file_name = request.args.get('file_name')
        file_path = os.path.join(DATA_DIR, file_name)
    except TypeError:
        return f'Не передан аргумент "file_name"', 400

    try:
        cmd1 = request.args.get('cmd1')
        cmd2 = request.args.get('cmd2')
        val1 = request.args.get('value1')
        val2 = request.args.get('value2')

        with open(file_path, 'r', encoding='utf-8') as file:
            data_file = file.read().rstrip().split('\n')
            response_cmd1 = data_processing(cmd1, val1, data_file)
            response_cmd2 = data_processing(cmd2, val2, response_cmd1)
            data_file = list(response_cmd2)
            return render_template('response.html', data_file=data_file)

    except FileNotFoundError:
        return f'File {file_name} does not exist', 400


if __name__ == "__main__":
    app.run(debug=True)
