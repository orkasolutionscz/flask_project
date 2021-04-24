from flask import Flask
from flask import render_template
from .database import articles

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
def view_articles_page():
    return render_template("articles_page.jinja", articles=articles.items())

@flask_app.route("/article/<int:art_id>")
def view_article_page(art_id):
    article = articles.get(art_id)
    return render_template("article_page.jinja", article=article)

