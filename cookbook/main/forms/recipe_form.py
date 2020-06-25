import flask_wtf
import wtforms
import wtforms.validators

from cookbook.main.models.categories import CATEGORIES_LIST


class RecipeForm(flask_wtf.FlaskForm):
    name = wtforms.StringField(
        "Recipe name", validators=[wtforms.validators.DataRequired()]
    )
    products = wtforms.SelectMultipleField(
        "Products", validators=[wtforms.validators.DataRequired()],
    )
    instruction = wtforms.StringField("Instruction")
    categories = wtforms.SelectMultipleField(
        "Categories", choices=[(c, c) for c in CATEGORIES_LIST]
    )
    submit = wtforms.SubmitField("Create")
