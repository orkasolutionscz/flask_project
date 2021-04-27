import os
from flask import Flask
from flask import render_template

from .models import db
from .mod_main import main
from .mod_blog import blog
from .mod_admin import admin



def create_flask_app():
    flask_app = Flask(__name__)
    flask_app.config.from_pyfile("/home/spravce/Python/flask_project/configs/default.py")
    if "MDBLOG_CONFIG" in os.environ:
        flask_app.config.from_envvar("MDBLOG_CONFIG")

    ## DB init
    db.init_app(flask_app)

    ## Registrace Blueprint
    flask_app.register_blueprint(main)
    flask_app.register_blueprint(blog)
    flask_app.register_blueprint(admin, url_prefix="/admin")

    @flask_app.errorhandler(500)
    def internal_server_error(error):
        return render_template("errors/500.jinja"), 500

    @flask_app.errorhandler(404)
    def internal_server_error(error):
        return render_template("errors/404.jinja"), 404

    return flask_app
