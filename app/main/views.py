from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response, jsonify
from .forms import SchoolForm
from ..models import MasterSchedule, Student, ClassTimes
from . import main

@main.route('/register/<school>', methods=['GET', 'POST'])
def register_form(school):
    form = SchoolForm()
    if form.validate_on_submit():
        return redirect(url_for('main.register_classes', school=school, science=form.science_choices.data,
															math=form.math_choices.data,
															history=form.history_choices.data,
															electives=form.elective_choices.data,
															english=form.english_choices.data))
    schedule = MasterSchedule(school)
    form.fill_classes(schedule)
    return render_template('register.html', school=school, user='user2', form=form)

@main.route('/landing/<school>', methods=['GET'])
def register_classes(school):
    student = Student(request.args, school)
    class_times = ClassTimes(request.args)
    return render_template('landing.html', school=school, class_times=class_times)
