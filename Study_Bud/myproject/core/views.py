from flask import render_template, Blueprint

core = Blueprint('core', __name__, template_folder='templates/core')


@core.route("/about")
def about():
    return render_template('about.html')


@core.route("/")
@core.route("/home")
def home():
    return render_template('home.html')
