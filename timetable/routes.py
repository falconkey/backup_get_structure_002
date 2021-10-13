import datetime
import os
#import flask
from flask import Flask, send_from_directory, render_template
from flask import Blueprint

app_001 = Blueprint('app_001', __name__, template_folder='templates', static_folder='static')
#app_001 = Blueprint('app_001', __name__)

#@app.route('/')
#def home_page():
#    return render_template('home_index.html')

@app_001.route('/tt')
def tt_index_page():
#    return ("show tt")
    return render_template('timetable/tt_index.html')

@app_001.route('/tt_dic_index')
def tt_dic_page():
    return render_template('timetable/tt_dic_index.html')

@app_001.route('/tt_cic_index')
def tt_cic_page():
    return render_template('timetable/tt_cic_index.html')

@app_001.route('/pdf_files/tt/ccbt21001.pdf') #the url you'll send the user to when he wants the pdf
def ccbt21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'ccbt21001.pdf')

@app_001.route('/pdf_files/tt/ccec21001.pdf') #the url you'll send the user to when he wants the pdf
def ccec21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'ccec21001.pdf')

@app_001.route('/pdf_files/tt/ccjn21001.pdf') #the url you'll send the user to when he wants the pdf
def pdfviewer():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'ccjn21001.pdf')

@app_001.route('/pdf_files/tt/ccpd21001.pdf') #the url you'll send the user to when he wants the pdf
def ccpd21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'ccpd21001.pdf')

@app_001.route('/pdf_files/tt/ccpm21001.pdf') #the url you'll send the user to when he wants the pdf
def ccpm21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'ccpm21001.pdf')

@app_001.route('/pdf_files/tt/ccpp21001.pdf') #the url you'll send the user to when he wants the pdf
def ccpp21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'ccpp21001.pdf')

@app_001.route('/pdf_files/tt/ccss21001.pdf') #the url you'll send the user to when he wants the pdf
def ccss21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'ccss21001.pdf')

@app_001.route('/pdf_files/tt/dcba21001.pdf') #the url you'll send the user to when he wants the pdf
def dcba21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcba21001.pdf')

@app_001.route('/pdf_files/tt/dcbp21001.pdf') #the url you'll send the user to when he wants the pdf
def dcbp21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcbp21001.pdf')

@app_001.route('/pdf_files/tt/dcbp21002.pdf') #the url you'll send the user to when he wants the pdf
def dcbp21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcbp21002.pdf')

@app_001.route('/pdf_files/tt/dcec21001.pdf') #the url you'll send the user to when he wants the pdf
def dcec21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcec21001.pdf')

@app_001.route('/pdf_files/tt/dcec21002.pdf') #the url you'll send the user to when he wants the pdf
def dcec21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcec21002.pdf')

@app_001.route('/pdf_files/tt/dcjn21001.pdf') #the url you'll send the user to when he wants the pdf
def dcjn21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcjn21001.pdf')

@app_001.route('/pdf_files/tt/dcjn21002.pdf') #the url you'll send the user to when he wants the pdf
def dcjn21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcjn21002.pdf')

@app_001.route('/pdf_files/tt/dcpd21001.pdf') #the url you'll send the user to when he wants the pdf
def dcpd21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpd21001.pdf')

@app_001.route('/pdf_files/tt/dcpd21002.pdf') #the url you'll send the user to when he wants the pdf
def dcpd21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpd21002.pdf')

@app_001.route('/pdf_files/tt/dcpm21001.pdf') #the url you'll send the user to when he wants the pdf
def dcpm21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpm21001.pdf')

@app_001.route('/pdf_files/tt/dcpp21001.pdf') #the url you'll send the user to when he wants the pdf
def dcpp21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpp21001.pdf')

@app_001.route('/pdf_files/tt/dcpp21002.pdf') #the url you'll send the user to when he wants the pdf
def dcpp21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcpp21002.pdf')

@app_001.route('/pdf_files/tt/dcss21001.pdf') #the url you'll send the user to when he wants the pdf
def dcss21001_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcss21001.pdf')

@app_001.route('/pdf_files/tt/dcss21002.pdf') #the url you'll send the user to when he wants the pdf
def dcss21002_page():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/timetable/pdf_files/tt/'
    return send_from_directory(filepath, 'dcss21002.pdf')


#if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=8080, debug=True)
