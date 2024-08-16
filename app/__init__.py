from flask import Flask
from .routes import APIRoutes
from .routes import app as main_blueprint
from .config import Config
from .extensions import db, jwt
from flask_restful import Api

def crear_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    api = Api(app)

    db.init_app(app)
    jwt.init_app(app)   

    api_routes = APIRoutes()
    api_routes.init_routes(api)

    app.register_blueprint(main_blueprint)

    return app
