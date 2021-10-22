from flask import Flask, Blueprint
from flask import Flask, render_template
from timetable.routes import app_001
from student_sv_record.routes import app_002


app = Flask(__name__)

@app.route('/')
def home_index_page():
#    return render_template('timetable/templates/timetable/index.html')
    return "<H1>Page is not ready"

app.register_blueprint(app_001)
app.register_blueprint(app_002)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
