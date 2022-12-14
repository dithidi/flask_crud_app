import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv('.env')

# Initialize db here to make it globally available
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    # Create and configure the application
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Make sure the instance folder is present
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    login_manager.init_app(app)

    # Initialize the database
    db.init_app(app)

    from . import models
    migrate.init_app(app, db)

    # Register the Blueprints
    from .blueprints import home
    from .blueprints import auth
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)

    return app
