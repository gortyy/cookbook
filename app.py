import os

import flask
import flask_migrate

import cookbook
from cookbook.main import models


app = cookbook.create_app(os.getenv("FLASK_CONFIG") or "default")
app.secret_key = os.getenv("FLASK_SECRET")
migrate = flask_migrate.Migrate(app, cookbook.db)


@app.errorhandler(404)
def page_not_found(e):
    return (flask.render_template("404.html"), 404)


@app.errorhandler(500)
def internal_server_error(e):
    return (flask.render_template("500.html"), 500)


@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=cookbook.db,
        Chef=models.Chef,
        Cookbook=models.Cookbook,
        Recipe=models.Recipe,
        Category=models.Category,
        Product=models.Product,
    )
