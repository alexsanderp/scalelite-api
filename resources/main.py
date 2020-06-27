from http import HTTPStatus

from flask_restful import Resource, reqparse
from scalelite import Scalelite
from env_vars import SCALELITE_BIN_PATH

scalelite = Scalelite(bin_path=SCALELITE_BIN_PATH)


class Status(Resource):
    @staticmethod
    def get():
        status = scalelite.status()
        return status, HTTPStatus.OK
