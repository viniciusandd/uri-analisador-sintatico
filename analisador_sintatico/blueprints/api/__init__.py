from flask import Blueprint
from flask_restful import Api
from .resources import AnalisadorSintatico

bp = Blueprint("analisador_sintatico", __name__, url_prefix="/api")

api = Api(bp)
api.add_resource(AnalisadorSintatico, "/analisador_sintatico")

def init_app(app):
    app.register_blueprint(bp)