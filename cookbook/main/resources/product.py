import flask


product_blueprint = flask.Blueprint("product", __name__)


@product_blueprint.route("/")
def products():
    pass


@product_blueprint.route("/<name>")
def product(name):
    pass
