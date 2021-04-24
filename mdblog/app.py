from flask import Flask
from flask import render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja", text='ahoj debile, jak je<')

@flask_app.route("/about")
def view_about_page():
    return render_template("about_page.jinja", text='ahoj debile, jak je<')

