from flask import Flask, Blueprint
from timetable.routes import app_001

app = Flask(__name__)

@app.route('/')
def home_index_page():
        return "Construction"

#app.register_blueprint(app_001, url_prefix='/templates/timetable')
#app.register_blueprint(app_001, url_prefix='/timetable')
app.register_blueprint(app_001)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
