from flask import Blueprint, render_template, url_for

bp = Blueprint("index", __name__, url_prefix='/index')

@bp.route('/')
def index():
    return render_template('index.html')