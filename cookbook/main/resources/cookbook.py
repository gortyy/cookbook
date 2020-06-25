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
    form.recipes.choices = [
        (recipe.name, recipe.name) for recipe in Recipe.get_all()
    ]
    if form.validate_on_submit():
        try:
            cookbook = Cookbook.add(form.name.data, recipes=form.recipes.data)
        except Exception as exc:
            flask.session["cookbook_error_type"] = "Could not create cookbook."
            flask.session["cookbook_error_msg"] = str(exc)
            return flask.redirect(flask.url_for(".failure"))

        flask.session["cookbook_name"] = cookbook.name
        return flask.redirect(flask.url_for(".added"))

    return flask.render_template("cookbook/create.html", form=form)


@cookbook_blueprint.route("/added")
def added():
    return flask.render_template("cookbook/success.html")


@cookbook_blueprint.route("/error")
def failure():
    return flask.render_template("cookbook/failure.html")
