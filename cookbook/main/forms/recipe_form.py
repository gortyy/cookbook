import flask_wtf
import wtforms
import wtforms.validators

from cookbook.main.models.categories import CATEGORIES_LIST


class RecipeBaseForm(flask_wtf.FlaskForm):
    products = wtforms.SelectMultipleField(
        "Products", validators=[wtforms.validators.DataRequired()],
    )
    instruction = wtforms.StringField("Instruction")
    categories = wtforms.SelectMultipleField(
        "Categories", choices=[(c, c) for c in CATEGORIES_LIST]
    )
    submit = wtforms.SubmitField("Create")


class RecipeSearchForm(RecipeBaseForm):
    pass


class RecipeCreateForm(RecipeBaseForm):
    name = wtforms.StringField(
        "Recipe name", validators=[wtforms.validators.DataRequired()]
    )
