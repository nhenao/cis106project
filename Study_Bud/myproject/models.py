# set up db inside __init__.py file in myproject folder
from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    schedule_posts = db.relationship(
        'SchedulePost', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class SchedulePost(db.Model):

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    day = db.Column(db.String(10), nullable=False)
    event = db.Column(db.String(150), nullable=False)

    def __init__(self, day, event, user_id):
        self.day = day
        self.event = event
        self.user_id = user_id


class Semester(db.Model):

    __tablename__ = 'semesters'

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    term = db.Column(db.String(10), nullable=False)
    year = db.Column(db.String(20), nullable=False)


class Courses(db.Model):

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    semester_id = db.Column(db.Integer, db.ForeignKey('semesters.id'))

    course_name = db.Column(db.String(30), nullable=False)
    professor = db.Column(db.String(50), nullable=False)

    semester = db.relationship(
        'Semester',
        backref=db.backref('courses', lazy='dynamic', collection_class=list))


class Assignments(db.Model):

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    duedate = db.Column(db.String(15), nullable=False)
    assignment = db.Column(db.String(150), nullable=False)
    course = db.Column(db.String(30), nullable=False)

    def __init__(self, duedate, assignment, course, user_id):
        self.duedate = duedate
        self.assignment = assignment
        self.course = course
        self.user_id = user_id
