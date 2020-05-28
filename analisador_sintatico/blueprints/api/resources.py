from flask import jsonify
from flask_restful import Resource

class AnalisadorSintatico(Resource):
    def get(self):
        return jsonify({"msg": "teste"})