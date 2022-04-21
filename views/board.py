from flask import Blueprint, redirect, render_template, request, url_for


bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route('/')
def board():
    return render_template('board.html')


@bp.route('/post')
def post():
    # id = request.args.get('id')
    return render_template('post.html')


@bp.route('/comment')
def comment():
    return render_template('comment.html')