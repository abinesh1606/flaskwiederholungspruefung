from flask_restx import fields

from .extensions import api 


post_model = api.model("Post", {
    "id": fields.Integer,
    "title": fields.String,
    "body": fields.String,
    "created":fields.DateTime,
    "author_id":fields.Integer,
})