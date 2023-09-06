from flask_restful import Resource

from api.app import api

class DefaultResource(Resource):
    def get(self):
        return {
            "message": "Hello, World!",
            "status": "success"
            }

api.add_resource(DefaultResource, "/", endpoint="home")
