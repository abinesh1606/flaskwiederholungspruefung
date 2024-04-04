from flask_restx import Resource, Namespace, abort
from .extensions import db
from .db_models import Post, User
from .api_models import post_model,post_input_model,post_update_model