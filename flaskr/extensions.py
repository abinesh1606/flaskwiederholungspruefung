from flask_login import  LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

api = Api(
        title='Blog Post API',
        description='API for adding, updating and deleting blog post.',
        doc='/docs/'
    )
db = SQLAlchemy()
login_manager = LginManager()