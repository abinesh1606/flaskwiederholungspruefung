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


@ns.route("/<int:id>")
class PostAPI(Resource):
    @ns.marshal_with(post_model)
    def get(self, id):
        """Get post by Id"""
        post = Post.query.get(id)
        if post:
            return post
        abort(404, "Post not found")

    @ns.expect(post_update_model)
    @ns.marshal_with(post_model)
    def patch(self, id):
        """Update post by Id"""
        if 'author_id' in ns.payload and not User.query.filter_by(id=ns.payload['author_id']).first():
            abort(400, "author_id doesn't exists")  
        post = Post.query.get(id)
        if post:
            if 'title' in ns.payload:
                post.title = ns.payload["title"]
            if 'body' in ns.payload:
                post.body = ns.payload["body"]
            if 'author_id' in ns.payload:
                post.author_id = ns.payload["author_id"]
            db.session.commit()
            return post
        abort(404, "Post not found")
    
    @ns.doc(responses={204: "Post deleted"})
    def delete(self, id):
        """Delete post by Id"""
        post = Post.query.get(id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return {}, 204
        abort(404, message="Post not found")
