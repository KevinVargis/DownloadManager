from flask import render_template
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import newdownload

from app import app

app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('Enter your (comma-separated) URLs', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    form = NameForm()
    if form.validate_on_submit():
        urls = form.name.data
        form.name.data = ""
        message = newdownload.download_links(urls)
    return render_template("index.html", form = form, messasge = message)


@app.route('/about')
def about():
    return render_template("about.html")