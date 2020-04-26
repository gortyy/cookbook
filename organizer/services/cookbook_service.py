from typing import List

from models import db
from models.cookbook_model import Recipe as RecipeModel


class Ingredient:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @classmethod
    def from_string(cls, ingredient):
        name, price = ingredient.split(":")
        return cls(name, float(price))

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f"{self.name}:{self.price}"

    def __hash__(self):
        return repr(self)


class Step:
    def __init__(self, instruction: str):
        self._instruction = instruction

    @property
    def instruction(self):
        return self._instruction

    def __str__(self):
        return self.instruction


class Recipe:
    def __init__(
        self, name: str, ingredients: List[Ingredient], steps: List[Step],
    ):
        self._name = name
        self._ingredients = ingredients
        self._steps = steps

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def name(self):
        return self._name

    @property
    def steps(self):
        return self._steps

    @classmethod
    def create(cls, name, ingredients, steps):
        ingredients = [Ingredient(**ingredient) for ingredient in ingredients]
        steps = [Step(**step) for step in steps]

        return cls(name, ingredients, steps)

    @classmethod
    def get(cls, name):
        recipe = RecipeModel.query.filter_by(name=name).one_or_none()
        if recipe is None:
            return None
        name = recipe.name
        ingredients = [
            Ingredient.from_string(ingredient)
            for ingredient in recipe.ingredients.split(",")
        ]
        steps = [Step(instruction) for instruction in recipe.steps.split(",")]

        return cls(name, ingredients, steps)

    def push(self):
        recipe = RecipeModel(
            self.name,
            ",".join(str(i) for i in self.ingredients),
            ",".join(str(s) for s in self.steps),
        )

        db.session.add(recipe)
        db.session.commit()

    def __repr__(self):
        return (
            f"INGREDIENTS: {','.join(str(i) for i in self.ingredients)},"
            f"STEPS: {','.join(str(s) for s in self.steps)}"
        )
