from flask_restx import Resource, Namespace, abort
from .extensions import db
from .db_models import Post, User
from .api_models import post_model,post_input_model,post_update_model

ns = Namespace("posts",description='POST operations')
    
    
@ns.route("/")
class PostListAPI(Resource):
    @ns.marshal_list_with(post_model)
    def get(self):
        """All Posts"""
        return Post.query.all()

    @ns.expect(post_input_model)
    @ns.marshal_with(post_model,code=201)
    def post(self):
        """Create post"""
        if 'author_id' in ns.payload and not User.query.filter_by(id=ns.payload['author_id']).first():
            abort(400, "author_id doesn't exists")  
        new_post = Post(
                title=ns.payload["title"],
                body=ns.payload["body"],
                author_id=ns.payload["author_id"]
        )
        db.session.add(new_post)
        db.session.commit()
        return new_post, 201