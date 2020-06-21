import flask_wtf
import wtforms
import wtforms.validators


class ProductForm(flask_wtf.FlaskForm):
    name = wtforms.StringField(
        "Product name", validators=[wtforms.validators.DataRequired()]
    )
    link = wtforms.StringField(
        "Link to shop", validators=[wtforms.validators.DataRequired()]
    )
    submit = wtforms.SubmitField("Create")
