from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from .database import articles

flask_app = Flask(__name__)
flask_app.secret_key = b'\xfcc\x01n\xed\xa9\x88\x9a\x08\xf3\x1a}R\xeb=/\\\xc1\xbc\xe4\x11,\xa2\xa2'

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")

@flask_app.route("/about/")
def view_about_page():
    return render_template("about_page.jinja")

@flask_app.route("/admin/")
def view_admin_page():
    if "logged" not in session:
        return redirect(url_for("view_login"))
    return render_template("admin_page.jinja")

@flask_app.route("/article/")
def view_articles_page():
    return render_template("articles_page.jinja", articles=articles.items())

@flask_app.route("/article/<int:art_id>")
def view_article_page(art_id):
    article = articles.get(art_id)
    if article:
        return render_template("article_page.jinja", article=article)
    return render_template("article_not_found.jinja", art_id=art_id)


@flask_app.route("/login/", methods=["GET"])
def view_login():
    return render_template("login.jinja")


@flask_app.route("/login/", methods=["POST"])
def login_user():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "admin":
        session["logged"] = True
        print(username, password, session["logged"])
        return redirect(url_for("view_admin_page"))
    else:
        return redirect(url_for("view_login"))

@flask_app.route("/logout/", methods=["POST"])
def logout_user():
    session.pop("logged")
    return redirect(url_for("view_welcome_page"))
