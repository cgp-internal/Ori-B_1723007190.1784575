from flask import Flask, render_template, request
import os
from models.pip_runner import run_pip

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        package = request.form.get('package')
        pip_commands = [f'pip install {package}']
        if run_pip(pip_commands):
            return f'Package {package} installed successfully!'
        else:
            return 'Error installing package...', 500
    return render_template('index.html')

if __name__ == '__main__':
    app.run()