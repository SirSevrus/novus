
from flask import Blueprint, render_template

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@errors_bp.app_errorhandler(405)
def method_not_allowed_error(error):
    return render_template('405.html'), 405
    