import flask_wtf
import wtforms
import wtforms.validators


class CookbookForm(flask_wtf.FlaskForm):
    name = wtforms.StringField(
        "Cookbook name", validators=[wtforms.validators.DataRequired()]
    )
    recipes = wtforms.SelectMultipleField(
        "Recipes", validators=[wtforms.validators.DataRequired()]
    )
    submit = wtforms.SubmitField("Create")
