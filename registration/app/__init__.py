from flask import Flask,render_template
from app.extensions import db, migrate, jwt
from app.routes.home_route import home_bp
from config import DevConfig
from flask_cors import CORS,cross_origin


def create_app(config_class=DevConfig):
    app = app = Flask(__name__,template_folder='templates')
    if config_class:
        app.config.from_object(config_class)
    app.static_folder = 'static'
    app.template_folder = 'templates'
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SECRET_KEY'] = 'df2bbac85c996454f92c0591b32c1e0e65983c5bb3c3711faae9addb32b5e279'
    app.config['JWT_TOKEN_LOCATION'] =  ["headers", "cookies", "json", "query_string"]
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
    app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'    
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    app.config["JWT_COOKIE_SECURE"] = False
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    print("----------------------entered in thr root---------------------------")
    @app.route('/',methods=['GET'])
    def sendtologin():
        return render_template('root.html')
    app.register_blueprint(home_bp)
    @app.after_request
    def after_request(response):
        #response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
        return response

    return app
