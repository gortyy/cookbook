import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


class TestConfig(Config):
    pass


class ProdConfig(Config):
    pass


config = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig,
    "default": DevConfig,
}
