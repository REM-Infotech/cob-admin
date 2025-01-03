from flask import current_app as app
from flask import redirect, url_for

from .auth import auth
from .dash import dash
from .index import index

__all__ = ["auth", "index", "dash"]


@app.route("/")
def redirect_login():

    return redirect(url_for("auth.login"))
