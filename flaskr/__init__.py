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
    

    


    
    

    
