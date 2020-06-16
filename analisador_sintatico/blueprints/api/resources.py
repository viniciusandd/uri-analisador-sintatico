from flask import jsonify
from flask_restful import Resource
from .parsers import retornar_parser


class AnalisadorSintatico(Resource):
    def get(self):
        parser = retornar_parser()
        args = parser.parse_args()
        sentenca = args['sentenca']        
        
