from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abkijajaoijsoakakalslslsl'
    #we need to tell flask that we have a blueprint that are containing some diferent views or different urls for out application , heres where they are .

    from .views import views
    from .auth import auth

    #now we register them to our app
    # the url-prefix is saying that , all of the URLs that are stored inside of the blueprints file, how am i going to access them, do I have to go to a prefix specifically? 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app