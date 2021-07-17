


from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from authz.config import Config



db = SQLAlchemy()
mg = Migrate()
api = Api()
from authz import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load config from env variables
    db.init_app(app)
    print(db)
    mg.init_app(app, db)
    api.init_app(app)
    return app
