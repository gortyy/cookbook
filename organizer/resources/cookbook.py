from flask_restx import fields, Namespace, reqparse, Resource

from organizer.services import cookbook_service as cs

cookbook = Namespace("cookbook")


ingredient_fields = cookbook.model(
    "Ingredient", {"name": fields.String, "price": fields.Float}
)

step_fields = cookbook.model("Step", {"instruction": fields.String})


recipe_model = cookbook.model(
    "Recipe",
    {
        "ingredients": fields.List(fields.Nested(ingredient_fields)),
        "steps": fields.List(fields.Nested(step_fields)),
    },
)


@cookbook.route("/<name>")
class Recipe(Resource):
    @cookbook.marshal_with(recipe_model)
    def get(self, name):
        recipe = cs.Recipe.get(name)
        if recipe:
            return recipe
        return "", 404

    @cookbook.expect(recipe_model)
    @cookbook.marshal_with(recipe_model)
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("ingredients", type=list, location="json")
        parser.add_argument("steps", type=list, location="json")

        args = parser.parse_args()
        recipe = cs.Recipe.create(
            name=name, ingredients=args["ingredients"], steps=args["steps"]
        )

        recipe.push()

        return recipe, 201
