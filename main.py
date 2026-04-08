import flask_cors from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    return app