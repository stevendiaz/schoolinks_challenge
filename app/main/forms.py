from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError

class SchoolForm(FlaskForm):
    science_choices = SelectField('Science', choices = [], validators = [Required()])
    math_choices = SelectField('Math', choices = [], validators = [Required()])
    history_choices = SelectField('History', choices = [], validators = [Required()])
    elective_choices = SelectField('Electives', choices = [], validators = [Required()])
    english_choices = SelectField('English', choices = [], validators = [Required()])
    submit = SubmitField('Submit')


    def fill_classes(self, classes):
        self.science_choices.choices = classes.science 
        self.math_choices.choices = classes.math 
        self.history_choices.choices = classes.history
        self.english_choices.choices = classes.english
        self.elective_choices.choices = classes.elective

    def class_times_are_unique(self):
        class_times = set([self.science_choices.data, self.math_choices.data, self.history_choices.data,
                            self.english_choices.data, self.elective_choices.data])
        return len(class_times) == 5

    def validate(self):
		if not self.class_times_are_unique():
			flash('Class times must be unique')
			return False
		return True
