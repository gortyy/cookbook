import flask

from cookbook.main.forms.cookbook_form import CookbookForm
from cookbook.main.models import Cookbook, Recipe

cookbook_blueprint = flask.Blueprint("cookbook", __name__)


@cookbook_blueprint.route("/")
def cookbooks():
    cookbooks = Cookbook.get_all()
    return flask.render_template("cookbook/all.html", cookbooks=cookbooks)


@cookbook_blueprint.route("/<name>")
def cookbook(name):
    if cookbook := Cookbook.get_by_name(name):
        return flask.render_template("cookbook/single.html", cookbook=cookbook)
    return flask.render_template("cookbook/not_found.html", name=name)


@cookbook_blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = CookbookForm()
    if form.validate_on_submit():
        cookbook_name = form.name.data
        recipes = [
            Recipe.get_by_name(recipe_name)
            for recipe_name in form.recipes.data.split(",")
        ]
        recipes = []
        missing_recipes = []
        for recipe_name in form.recipes.data.strip().split(", "):
            if recipe := Recipe.get_by_name(recipe_name):
                recipes.append(recipe)
            else:
                missing_recipes.append(recipe_name)
        missing_recipes = [
            missing for missing in missing_recipes if missing != ""
        ]
        if missing_recipes:
            flask.session["cookbook_error_type"] = "Missing recipes"
            flask.session["missing_recipes"] = ", ".join(missing_recipes)
            return flask.redirect(flask.url_for(".failure"))

        cookbook = Cookbook.add(cookbook_name, recipes)
        flask.session["cookbook_name"] = cookbook.name
        return flask.redirect(flask.url_for(".added"))

    return flask.render_template("cookbook/create.html", form=form)


@cookbook_blueprint.route("/added")
def added():
    return flask.render_template("cookbook/success.html")


@cookbook_blueprint.route("/error")
def failure():
    return flask.render_template("cookbook/failure.html")
