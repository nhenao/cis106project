from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, TextAreaField, StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class CourseSetup(Form):
  course = StringField('Course Name')
  professor = StringField('Professsor')


class MainSetup(FlaskForm):
  term = SelectField('Select Term', validators=[DataRequired()],
                     choices=[('Fall', 'Fall'),
                              ('Winter', 'Winter'),
                              ('Spring', 'Spring'),
                              ('Summer', 'Summer')])
  year = StringField('Enter Year of Semester', validators=[DataRequired()])
  courses = FieldList(
      FormField(CourseSetup),
      min_entries=1,
      max_entries=10)

  submit = SubmitField('Submit')


class Assignments(FlaskForm):
  duedate = DateField('Enter Due Date', validators=[
                      DataRequired()], format='%Y-%m-%d')
  assignment = TextAreaField(
      'Enter Assignement', validators=[DataRequired()])
  course = SelectField('Select Course', validators=[DataRequired()])
  submit = SubmitField('Post Assignment')
