
#importing required packages
from flask import Flask, render_template
import pandas as pd
app = Flask(__name__, template_folder="Templates")
@app.route('/', methods =['POST', 'GET'])

def home():
        return render_template('index.html',message="hi")
if __name__ == '__main__':
    app.run(debug = True)