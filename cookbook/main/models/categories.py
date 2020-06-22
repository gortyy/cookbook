import enum


class Categories(enum.Enum):
    burger = "burger"
    dumplings = "dumplings"


CATEGORIES_LIST = [c.value for c in Categories]
