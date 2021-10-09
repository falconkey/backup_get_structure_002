# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_render_template]
# [START gae_python3_render_template]
import datetime
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_index.html')

@app.route('/tt')
def tt_home_page():
    return render_template('tt_index.html')

@app.route('/tt_dic_index')
def tt_dic_page():
    return render_template('tt_dic_index.html')

@app.route('/tt_cic_index')
def tt_cic_page():
    return render_template('tt_cic_index.html')

@app.route('/pdf_files/tt/ccbt21001.pdf') #the url you'll send the user to when he wants the pdf
def ccbt21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccbt21001.pdf')

@app.route('/pdf_files/tt/ccec21001.pdf') #the url you'll send the user to when he wants the pdf
def ccec21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccec21001.pdf')

@app.route('/pdf_files/tt/ccjn21001.pdf') #the url you'll send the user to when he wants the pdf
def pdfviewer():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccjn21001.pdf')

@app.route('/pdf_files/tt/ccpd21001.pdf') #the url you'll send the user to when he wants the pdf
def ccpd21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccpd21001.pdf')

@app.route('/pdf_files/tt/ccpm21001.pdf') #the url you'll send the user to when he wants the pdf
def ccpm21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccpm21001.pdf')

@app.route('/pdf_files/tt/ccpp21001.pdf') #the url you'll send the user to when he wants the pdf
def ccpp21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccpp21001.pdf')

@app.route('/pdf_files/tt/ccss21001.pdf') #the url you'll send the user to when he wants the pdf
def ccss21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'ccss21001.pdf')

@app.route('/pdf_files/tt/dcba21001.pdf') #the url you'll send the user to when he wants the pdf
def dcba21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcba21001.pdf')

@app.route('/pdf_files/tt/dcbp21001.pdf') #the url you'll send the user to when he wants the pdf
def dcbp21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcbp21001.pdf')

@app.route('/pdf_files/tt/dcbp21002.pdf') #the url you'll send the user to when he wants the pdf
def dcbp21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcbp21002.pdf')

@app.route('/pdf_files/tt/dcec21001.pdf') #the url you'll send the user to when he wants the pdf
def dcec21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcec21001.pdf')

@app.route('/pdf_files/tt/dcec21002.pdf') #the url you'll send the user to when he wants the pdf
def dcec21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcec21002.pdf')

@app.route('/pdf_files/tt/dcjn21001.pdf') #the url you'll send the user to when he wants the pdf
def dcjn21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcjn21001.pdf')

@app.route('/pdf_files/tt/dcjn21002.pdf') #the url you'll send the user to when he wants the pdf
def dcjn21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcjn21002.pdf')

@app.route('/pdf_files/tt/dcpd21001.pdf') #the url you'll send the user to when he wants the pdf
def dcpd21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpd21001.pdf')

@app.route('/pdf_files/tt/dcpd21002.pdf') #the url you'll send the user to when he wants the pdf
def dcpd21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpd21002.pdf')

@app.route('/pdf_files/tt/dcpm21001.pdf') #the url you'll send the user to when he wants the pdf
def dcpm21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpm21001.pdf')

@app.route('/pdf_files/tt/dcpp21001.pdf') #the url you'll send the user to when he wants the pdf
def dcpp21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpp21001.pdf')

@app.route('/pdf_files/tt/dcpp21002.pdf') #the url you'll send the user to when he wants the pdf
def dcpp21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpp21002.pdf')

@app.route('/pdf_files/tt/dcss21001.pdf') #the url you'll send the user to when he wants the pdf
def dcss21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcss21001.pdf')

@app.route('/pdf_files/tt/dcss21002.pdf') #the url you'll send the user to when he wants the pdf
def dcss21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf_files/tt/'
    return send_from_directory(filepath, 'dcss21002.pdf')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
