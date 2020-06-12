import os

import flask_migrate

import cookbook
import cookbook.main.models as models


app = cookbook.create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = flask_migrate.Migrate(app, cookbook.db)


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=cookbook.db,
        Chef=models.Chef,
        Cookbook=models.Cookbook,
        Recipe=models.Recipe,
        Category=models.Category,
        Product=models.Product,
    )