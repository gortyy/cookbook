from flask import Flask

from organizer.models import db
from organizer.resources import api


def create_organizer():
    organizer = Flask(__name__)
    organizer.config.from_object("config.Config")

    db.init_app(organizer)
    api.init_app(organizer)

    app_context = organizer.app_context()
    app_context.push()
    db.create_all()
    app_context.pop()

    return organizer


if __name__ == "__main__":
    organizer = create_organizer()
    organizer.run(debug=True, port=5000)
