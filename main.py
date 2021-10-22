from flask import Flask, Blueprint
from flask import Flask, render_template
from mainhome.routes import app_000
from timetable.routes import app_001
from student_sv_record.routes import app_002

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.register_blueprint(app_000)
app.register_blueprint(app_001)
app.register_blueprint(app_002)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
