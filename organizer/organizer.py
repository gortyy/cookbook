from flask import Flask

from models import db
from resources import api


if __name__ == "__main__":
    organizer = Flask(__name__)
    organizer.config.from_object("config.Config")

    db.init_app(organizer)
    api.init_app(organizer)

    app_context = organizer.app_context()
    app_context.push()
    db.create_all()
    app_context.pop()

    organizer.run(debug=True, port=5000)
