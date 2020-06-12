from cookbook import db


class Chef(db.Model):
    __tablename__ = "chefs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))

    cookbooks = db.relationship("Cookbook", backref="chef")


class Cookbook(db.Model):
    __tablename__ = "cookbooks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    chef_id = db.Column(db.Integer, db.ForeignKey("chefs.id"))


cookbook_recipe_association = db.Table(
    "cookbook_recipe_association",
    db.Column("cookbook_id", db.Integer, db.ForeignKey("cookbooks.id")),
    db.Column("recipe_id", db.Integer, db.ForeignKey("recipes.id")),
)

recipe_product_association = db.Table(
    "recipe_product_association",
    db.Column("recipe_id", db.Integer, db.ForeignKey("recipes.id")),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id")),
)

recipe_category_association = db.Table(
    "recipe_category_association",
    db.Column("recipe_id", db.Integer, db.ForeignKey("recipes.id")),
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id")),
)


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    instruction = db.Column(db.String(2048), nullable=False)

    cookbooks = db.relationship(
        "Cookbook",
        secondary=cookbook_recipe_association,
        backref=db.backref("recipes"),
    )


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

    recipes = db.relationship(
        "Recipe",
        secondary=recipe_category_association,
        backref=db.backref("categories"),
    )


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    shop_link = db.Column(db.String(256), nullable=False)

    recipes = db.relationship(
        "Recipe",
        secondary=recipe_product_association,
        backref=db.backref("products"),
    )
