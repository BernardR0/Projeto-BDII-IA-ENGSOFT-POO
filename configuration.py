from routes.home import home_route
from routes.assistidos import assistidos_route
from routes.abrigos import abrigos_route
from routes.operadores import operadores_route
from database.database import db

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(assistidos_route,  url_prefix='/assistidos')
    app.register_blueprint(abrigos_route,  url_prefix='/abrigos')
    app.register_blueprint(operadores_route,  url_prefix='/operadores')    

def configure_db():
    db.connect()