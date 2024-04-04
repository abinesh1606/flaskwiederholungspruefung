from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask_login import login_user,logout_user
from .db_models import User
from .extensions import db
from sqlalchemy import exc

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user. 
     Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                new_user = User(
                    username=username,
                    password=generate_password_hash(password)
                )
                db.session.add(new_user)
                db.session.commit()
                except exc.IntegrityError:
                # if any error occurs it rolls back to previous state
                db.session.rollback()
                # The username was already taken, which caused the
                # commit to fail. Show a validation error.
                error = f"User {username} is already registered."
            else:
                # Success, go to the login page.
                return redirect(url_for("auth.login"))
        
        flash(error)

    return render_template("auth/register.html")

@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by using login_user from flask-login."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        remember_me = True if request.form.get('remember_me') else False

         error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user.password, password):
            error = "Incorrect password."

            if error is None:
            # login user using flask-login method
            login_user(user, remember=remember_me)
            return redirect(url_for("index"))




