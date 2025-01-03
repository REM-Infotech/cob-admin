"""
This module defines the authentication routes for the application.
Blueprint:
    auth (Blueprint): The authentication blueprint with the template folder set to the 'templates' directory.
Routes:
    /login (methods=["GET", "POST"]): Handles user login functionality.
"""

from pathlib import Path

from flask import Blueprint

path_template = Path(__file__).parent.resolve().joinpath("templates")
auth = Blueprint("auth", __name__, template_folder=path_template)


@auth.route("/login", methods=["GET", "POST"])
def login():

    return "<h1>hello, world!</h1>"
