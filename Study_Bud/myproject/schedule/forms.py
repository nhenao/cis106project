from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class ScheduleForm(FlaskForm):
  day = SelectField('Select Day',
                    validators=[DataRequired()],
                    choices=[('Monday', 'Monday'),
                             ('Tuesday', 'Tuesday'),
                             ('Wednesday', 'Wednesday'),
                             ('Thursday', 'Thursday'),
                             ('Friday', 'Friday'),
                             ('Saturday', 'Saturday'),
                             ('Sunday', 'Sunday')])
  event = TextAreaField('Schdeule Post',
                        validators=[DataRequired()])
  submit = SubmitField('Submit')
