import flask

from cookbook.main.forms.product_form import ProductForm
from cookbook.main.models import Product

product_blueprint = flask.Blueprint("product", __name__)


@product_blueprint.route("/")
def products():
    products = Product.get_all()
    return flask.render_template("product/all.html", products=products)


@product_blueprint.route("/<name>")
def product(name):
    if product := Product.get_by_name(name):
        return flask.render_template("product/single.html", product=product)
    return flask.render_template("product/not_found.html", name=name)


@product_blueprint.route("/added")
def added():
    return flask.render_template("product/success.html")


@product_blueprint.route("/error")
def failure():
    return flask.render_template("product/failure.html")


@product_blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = ProductForm()
    if form.validate_on_submit():
        product_name = form.name.data
        link = form.link.data
        try:
            product = Product.add(product_name, link)
        except Exception as exc:
            flask.session["product_error_type"] = "Failed adding product."
            flask.session["product_exception"] = str(exc)
            return flask.redirect(flask.url_for(".failure"))
        else:
            flask.session["product_name"] = product.name
            return flask.redirect(flask.url_for(".added"))

    return flask.render_template("product/create.html", form=form)
