from flask import Flask, Blueprint
from src import app_config
from flask_cors import CORS
from src.routes.api import api


def create_flask_app():
    app = Flask(__name__)
    CORS(app)
    # app.config.from_object(app_config)
    route1 = Blueprint('route1', __name__,template_folder='template')
    api(route1)
    app.register_blueprint(route1, url_prefix='/app')
    return app


app = create_flask_app()
if __name__ == '__main__':
    app.run(debug=True)
