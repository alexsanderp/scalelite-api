from http import HTTPStatus

from flask_restful import Resource, reqparse
from scalelite import Scalelite
from env_vars import SCALELITE_BIN_PATH

scalelite = Scalelite(bin_path=SCALELITE_BIN_PATH)


class Servers(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str, required=True)
        parser.add_argument('secret', type=str, required=True)
        parser.add_argument('load_multiplier', type=float)
        args = parser.parse_args()
        server_id = scalelite.add_server(
            url=args['url'],
            secret=args['secret'],
            load_multiplier=args['load_multiplier']
        )
        return {"server_id": server_id}, HTTPStatus.OK


class Server(Resource):
    @staticmethod
    def put(id):
        parser = reqparse.RequestParser()
        parser.add_argument('load_multiplier', type=float)
        args = parser.parse_args()
        if args['load_multiplier']:
            scalelite.set_load_multiplier_server(id, args['load_multiplier'])
        return None, HTTPStatus.OK

    @staticmethod
    def delete(id):
        scalelite.remove_server(id)
        return None, HTTPStatus.OK


class ServerEnable(Resource):
    @staticmethod
    def post(id):
        scalelite.enable_server(id)
        return None, HTTPStatus.OK


class ServerDisable(Resource):
    @staticmethod
    def post(id):
        scalelite.disable_server(id)
        return None, HTTPStatus.OK


class ServerPanic(Resource):
    @staticmethod
    def post(id):
        scalelite.panic_server(id)
        return None, HTTPStatus.OK
