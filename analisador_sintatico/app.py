from flask import Flask

from analisador_sintatico.ext import configuracao
from analisador_sintatico.ext import cors
from analisador_sintatico.blueprints import webui

def create_app():
    app = Flask(__name__)
    configuracao.init_app(app)
    cors.init_app(app)
    webui.init_app(app)
    return app