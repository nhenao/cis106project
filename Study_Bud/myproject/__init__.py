import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

######################
# DataBase Setup #####
######################


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#######################
# Login Config ########
#######################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'


from myproject.users.views import users
from myproject.schedule.views import schedule_blueprint
from myproject.assignments.views import assignments_blueprint
from myproject.tasks.views import tasks_blueprint
from myproject.error_pages.handlers import error_pages
from myproject.core.views import core

app.register_blueprint(schedule_blueprint, url_prefix='/schedule')
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(assignments_blueprint, url_prefix='/assignments')
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')
app.register_blueprint(error_pages)
app.register_blueprint(core)
