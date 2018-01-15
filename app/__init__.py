import os
from flask import Flask
from flask_login import LoginManager

from config import app_config
from flask_sqlalchemy import SQLAlchemy


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "employee.db"))

db = SQLAlchemy()


# initialize the app
app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'adsadshjhsjdh878isjk999'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'adminlogin'

from app import views

