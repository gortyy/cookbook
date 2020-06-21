import flask


recipe_blueprint = flask.Blueprint("recipe", __name__)


@recipe_blueprint.route("/")
def recipes():
    pass


@recipe_blueprint.route("/<name>")
def recipe(name):
    pass
