import flask

from cookbook.main.forms.recipe_form import RecipeForm
from cookbook.main.models import Product, Recipe


recipe_blueprint = flask.Blueprint("recipe", __name__)


@recipe_blueprint.route("/")
def recipes():
    recipes = Recipe.get_all()
    return flask.render_template("recipe/all.html", recipes=recipes)


@recipe_blueprint.route("/<name>")
def recipe(name):
    if recipe := Recipe.get_by_name(name):
        print(recipe.products)
        return flask.render_template("recipe/single.html", recipe=recipe)
    return flask.render_template("recipe/not_found.html", name=name)


@recipe_blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = RecipeForm()
    form.products.choices = _product_names()
    if form.validate_on_submit():
        try:
            recipe = Recipe.add(
                name=form.name.data,
                products=form.products.data,
                instruction=form.instruction.data,
                categories=form.categories.data,
            )
        except Exception as exc:
            flask.session["recipe_error_type"] = "Could not create recipe"
            flask.session["recipe_error_msg"] = str(exc)
            return flask.redirect(flask.url_for(".failure"))

        flask.session["recipe_name"] = recipe.name
        return flask.redirect(flask.url_for(".added"))

    return flask.render_template("recipe/create.html", form=form)


@recipe_blueprint.route("/added")
def added():
    return flask.render_template("recipe/success.html")


@recipe_blueprint.route("/error")
def failure():
    return flask.render_template("recipe/failure.html")


def _product_names():
    all_products = Product.get_all()
    return [(product.name, product.name) for product in all_products]
