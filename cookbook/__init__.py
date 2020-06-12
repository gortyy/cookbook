import flask
import flask_bootstrap
import flask_mail
import flask_sqlalchemy

from config import config


bootstrap = flask_bootstrap.Bootstrap()
mail = flask_mail.Mail()
db = flask_sqlalchemy.SQLAlchemy()


def create_app(config_name):
    app = flask.Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    return app
