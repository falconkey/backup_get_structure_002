import datetime
import os
#import flask
from flask import Flask, send_from_directory, render_template
from flask import Blueprint

app_000 = Blueprint('app_000', __name__, template_folder='templates', static_folder='static')

@app_000.route('/')
def first_home_page():
    return render_template('mainhome/index.html')

#if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=8080, debug=True)
