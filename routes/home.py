from flask import Blueprint, render_template, url_for

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
# Home route serving the flask server's '/' route.
def home():
    return render_template('index.html', tl="Homepage")
