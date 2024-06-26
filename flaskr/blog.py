from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify
from werkzeug.exceptions import abort
from flask_login import login_required
from flask_login import current_user
from .db_models import Post, Like
from .extensions import db

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    posts = Post.query.order_by(Post.created.desc()).all()
    return render_template("blog/index.html", posts=posts)


def get_post(id, check_author=True):
    """Get a post and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post = Post.query.filter_by(id=id).first()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post.author_id != current_user.id:
        abort(403)

    return post


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            new_post = Post(
                title=title,
                body=body,
                author_id=current_user.id
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body
            db.session.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/update.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    Post.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for("blog.index"))


@bp.route("/like/<int:id>", methods=['POST'])
@login_required
def post_like(id):
    """Like or unlike a post.
    
    Args:
        id (int): The ID of the post to like or unlike.
        
    Returns:
        Response: A JSON response containing the updated number of likes for the post
        and whether the current user has liked the post.
    """
    post = get_post(id,check_author=False)
    
    like = Like.query.filter_by(author=current_user, post_id=id).first()

    if like:
        db.session.delete(like)
        liked = False
    else:
        new_like = Like(author=current_user, post_id=id)
        db.session.add(new_like)
        liked = True

    db.session.commit()
    return jsonify({"likes": len(post.likes), "liked": liked })