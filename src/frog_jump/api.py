from flask import request
from flask_restful import Resource
from frog_jump.serializers import request_payload

from frog_jump.services import get_jump_index


class FrogJumpAPI(Resource):
    def post(self):
        json = request.get_json()
        data = request_payload.load(json)
        jump_at = get_jump_index(end_of_river=data['river_length'], leaves_list=data['leave_lists'])
        if (jump_at > 0):
            msg = 'Frog can jump'
        else:
            msg = 'Frog cannot jump'
        res = {
            'msg': msg,
            'jump_at': jump_at
        }
        return res
