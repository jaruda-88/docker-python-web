from flask import Blueprint, render_template, request


bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route('/')
def board():
    return render_template('board.html')


@bp.route('/post')
def post():
    # id = request.args.get('id')
    return render_template('post.html')