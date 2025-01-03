"""
This module initializes the 'cobrancas' Blueprint for the Flask application.

It sets up the Blueprint with the name 'cob' and specifies the template folder
relative to the current file's location.

Imports:
    Path (pathlib): Provides classes to handle filesystem paths.
    Blueprint, abort, make_response, render_template (flask): Flask utilities for creating blueprints and handling HTTP responses.
    login_required (flask_login): Decorator to require user login for specific routes.

Attributes:
    template_folder (Path): The path to the templates directory for this Blueprint.
    cob (Blueprint): The Blueprint instance for the 'cobrancas' module.
"""

from pathlib import Path

from flask import Blueprint, abort, render_template
from flask_login import login_required

template_folder = Path(__file__).parent.resolve().joinpath("templates")
cob = Blueprint(
    "cob", __name__, template_folder=template_folder, url_prefix="/cobrancas"
)


@cob.get("/dashboard")
@login_required
def dashboard():

    try:
        return render_template("cobrancas.html")
    except Exception as e:
        abort(500, description=str(e))
