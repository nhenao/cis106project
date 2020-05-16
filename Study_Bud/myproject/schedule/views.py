# my project/schedule/views.py
from flask import Blueprint, render_template, redirect, url_for, flash
from myproject.schedule.forms import ScheduleForm
from flask_login import current_user, login_required
from myproject import db
from myproject.models import SchedulePost


schedule_blueprint = Blueprint('schedule',
                               __name__,
                               template_folder='templates/schedule')


@schedule_blueprint.route("/add", methods=['GET', 'POST'])
@login_required
def add():
    form = ScheduleForm()

    if form.validate_on_submit():
        schedule_post = SchedulePost(user_id=current_user.id,
                                     day=form.day.data,
                                     event=form.event.data)
        db.session.add(schedule_post)
        db.session.commit()
        flash('Successfully added to your schedule!')
        return redirect(url_for('schedule.posts'))

    return render_template('add.html', title='Schedule', form=form)


@schedule_blueprint.route("/posts")
@login_required
def posts():
    schedule_posts = SchedulePost.query.filter_by(user_id=current_user.id)

    data = dict()
    for post in schedule_posts:
        try:
            data[post.day].append(post.event)
        except Exception:
            data[post.day] = [post.event]
    return render_template('posts.html', title='Schedule', data=data)
