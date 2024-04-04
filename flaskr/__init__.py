import os
from flask import Flask,Blueprint


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, "flaskr.sqlite"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    
    
    
    app.config['RESTX_MASK_SWAGGER'] = False

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    from .extensions import db,login_manager,api
    blueprint = Blueprint('api', __name__, url_prefix='/api')

    api.init_app(blueprint)
    from .resources import ns
    api.add_namespace(ns)
    
    db.init_app(app)
    login_manager.init_app(app)
    
    from .db_models import User
    
    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(int(user_id))

    
    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(int(user_id))

    # apply the blueprints to the app
    from . import auth
    from . import blog

    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(blueprint)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app
