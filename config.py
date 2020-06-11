class Config:
    pass


class DevConfig(Config):
    pass


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
