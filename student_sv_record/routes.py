import datetime
import os
#import flask
from flask import Flask, send_from_directory, render_template
from flask import Blueprint

app_002 = Blueprint('app_002', __name__, template_folder='templates', static_folder='static')
#app_001 = Blueprint('app_001', __name__)

#@app_001.route('/')
#def first_home_page():
#    return render_template('timetable/index.html')

@app_002.route('/zzz')
def zzz_page():
    return ("sleepy")
#    return render_template('timetable/tt_index.html')


#if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=8080, debug=True)
