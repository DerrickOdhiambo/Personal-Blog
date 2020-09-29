from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from blog.models import Email

class EmailSubscriptionForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "Email..."})
    submit = SubmitField('Subscribe')

    def validate_email(self, email):
      user = Email.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError('You have already subscibed!')