import flask_wtf
import wtforms
import wtforms.validators


class CookbookForm(flask_wtf.FlaskForm):
    name = wtforms.StringField(
        "Cookbook name", validators=[wtforms.validators.DataRequired()]
    )
    recipes = wtforms.StringField("Recipes")
    submit = wtforms.SubmitField("Create")
