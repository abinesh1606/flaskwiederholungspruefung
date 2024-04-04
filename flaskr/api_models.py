from flask_restx import fields

from .extensions import api 


post_model = api.model("Post", {
    "id": fields.Integer,
    "title": fields.String,
    "body": fields.String,
    "created":fields.DateTime,
    "author_id":fields.Integer,
})
post_input_model = api.model("PostInput", {
    "title": fields.String(required=True, description="Post title"),
    "body": fields.String(required=True, description="Post description"),
    "author_id": fields.Integer(required=True, description="Author id"),
})

post_update_model = api.model("PostUpdate", {
    "title": fields.String,
    "body": fields.String,
    "author_id": fields.Integer,
})