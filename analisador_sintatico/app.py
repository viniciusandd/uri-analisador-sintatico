from flask import Flask

from analisador_sintatico.ext import configuracao
from analisador_sintatico.ext import cors
from analisador_sintatico.blueprints import web
from analisador_sintatico.blueprints import api

def create_app():
    app = Flask(__name__)
    configuracao.init_app(app)
    cors.init_app(app)
    web.init_app(app)
    api.init_app(app)
    return app