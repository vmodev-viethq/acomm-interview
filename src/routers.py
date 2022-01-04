from flask_restful import Api
from frog_jump.api import FrogJumpAPI

api = Api()
api.add_resource(FrogJumpAPI, '/')
