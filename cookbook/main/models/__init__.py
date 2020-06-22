from cookbook import db


class Chef(db.Model):
    __tablename__ = "chefs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))

    cookbooks = db.relationship("Cookbook", backref="chef")

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


class Cookbook(db.Model):
    __tablename__ = "cookbooks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    chef_id = db.Column(db.Integer, db.ForeignKey("chefs.id"))

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def add(cls, name, recipes=None):
        if recipes is None:
            recipes = []
        cookbook = cls(name=name, recipes=recipes)
        db.session.add(cookbook)
        db.session.commit()

        return cookbook


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

    @classmethod
    def add(cls, name, instruction, categories=None, products=None):
        if categories is None:
            categories = []
        if products is None:
            products = []

        recipe = cls(
            name=name,
            instruction=instruction,
            categories=categories,
            products=products,
        )

        db.session.add(recipe)
        db.session.commit()

        return recipe

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

    recipes = db.relationship(
        "Recipe",
        secondary=recipe_category_association,
        backref=db.backref("categories"),
    )

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()


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

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def add(cls, name, shop_link=None):
        product = cls(name=name, shop_link=shop_link)
        db.session.add(product)
        db.session.commit()

        return product
