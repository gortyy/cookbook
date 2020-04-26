from flask_restx import Api

from .cookbook import cookbook

api = Api(title="organizer", version="0.1.0")
api.add_namespace(cookbook)
