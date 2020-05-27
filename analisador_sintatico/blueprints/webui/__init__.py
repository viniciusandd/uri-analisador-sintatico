from flask import Blueprint

from .views import index

bp = Blueprint(
    "webui", 
    __name__, 
    template_folder="templates", 
    static_folder='static', 
    static_url_path='/analisador_sintatico.webui.static'
)

bp.add_url_rule("/", view_func=index)

def init_app(app):
    app.register_blueprint(bp)