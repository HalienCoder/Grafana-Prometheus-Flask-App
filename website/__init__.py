from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from prometheus_client import Counter, Summary, generate_latest
from flask import Response, request
import time

db= SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', f'sqlite:///{DB_NAME}')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

    db.init_app(app)

    #we need to tell flask that we have a blueprint that are containing some diferent views or different urls for out application , heres where they are .

    
    from .views import views
    from .auth import auth

    #now we register them to our app
    # the url-prefix is saying that , all of the URLs that are stored inside of the blueprints file, how am i going to access them, do I have to go to a prefix specifically? 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note

     #we import the models because , when we import them, it will run the file once and then it will create the tables in the database.

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #wehre to redirect user if theyre not logged in?
    login_manager.init_app(app)

    #this line tells flask how we are going to load the user from the database
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    REQUEST_COUNT = Counter("app_requests_total", "Total number of requests", ['method', 'endpoint'])
    REQUEST_LATENCY = Summary("app_request_latency_seconds", "Request latency in seconds", ['endpoint'])

    @app.before_request
    def before_request():
        request.start_time = time.time()

    @app.after_request
    def after_request(response):
        if request.path != '/metrics':
            resp_time = time.time() - request.start_time
            REQUEST_LATENCY.labels(endpoint=request.path).observe(resp_time)
            REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
        return response

    @app.route('/metrics')
    def metrics():
        return Response(generate_latest(), mimetype='text/plain')

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        print("Creating database...")
        with app.app_context():  # Push the app context
            db.create_all()
        print('Created database!')
    else:
        print("Database already exists.")