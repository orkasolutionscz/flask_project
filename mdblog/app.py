from flask import Flask
from flask import render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")

@flask_app.route("/about/")
def view_about_page():
    return render_template("about_page.jinja")

@flask_app.route("/admin/")
def view_admin_page():
    return render_template("admin_page.jinja")

@flask_app.route("/article/")
def view_article_page():
    return render_template("article_page.jinja")

