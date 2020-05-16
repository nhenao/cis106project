from flask import Blueprint, render_template, redirect, url_for, flash
from myproject.assignments.forms import MainSetup, CourseSetup, Assignments
from flask_login import current_user, login_required
from myproject import db
from myproject.models import Semester, Courses, Assignments


assignments_blueprint = Blueprint('assignments',
                                  __name__,
                                  template_folder='templates/assignments')


@assignments_blueprint.route("/assignments")
@login_required
def assignments():
    assignments = AddAssignments.query.filter_by(user_id=current_user.id)

    data = dict()
    for post in assignments:
        try:
            data[post.course].append(post.assignments, post.duedate)
        except Exception:
            data[post.course] = [post.assignments]
    return render_template('assignments.html', title='Assignments', data=data)


@assignments_blueprint.route("/setup", methods=['GET', 'POST'])
@login_required
def setup():
    form = MainSetup()

    if form.validate_on_submit():
            # Create semester
        new_semester = Semester()

        db.session.add(new_semester)

        for course in form.courses.data:
            new_course = Courses(**course)

            # Add course to semester
            new_semester.courses.append(new_course)

        db.session.commit()

    semesters = Semester.query

    return render_template('setup.html', title='Assignments', form=form, semesters=semesters)


@assignments_blueprint.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        add = AddAssignments(user_id=current_user.id,
                             duedate=form.duedate.data,
                             assignment=form.assignment.data,
                             course=form.course.data)
        db.session.add(add)
        db.session.commit()
        flash('Successfully posted to your assignments!')
        return redirect(url_for('assignments.assignments'))

    return render_template('addassignment.html', title='Assignments', form=form)
