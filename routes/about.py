from flask import Blueprint

about_bp = Blueprint('about', __name__)

@about_bp.route('/about')
def about():
    return "This is the About page!"
