from flask import Blueprint, render_template

bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route('/')
def board():
    return render_template('board.html')