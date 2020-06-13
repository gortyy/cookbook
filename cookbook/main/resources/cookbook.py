import flask

from cookbook.main.models import Cookbook

cookbook_blueprint = flask.Blueprint("cookbook", __name__)


@cookbook_blueprint.route("/")
def cookbooks():
    return {
        "message": (
            "All cookbooks: "
            f"{[cookbook.name for cookbook in Cookbook.get_all()]}"
        )
    }


@cookbook_blueprint.route("/<name>")
def cookbook(name):
    cookbook = Cookbook.get_by_name(name)

    if cookbook:
        msg = f"Found cookbook {cookbook.name}."
    else:
        msg = "Cookbook not found."

    return {"message": msg}
