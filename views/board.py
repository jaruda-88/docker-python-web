from flask import Blueprint, render_template, request


bp = Blueprint('board', __name__, url_prefix='/board')

@bp.route('/')
def board():
    return render_template('board.html')


@bp.route('/detail')
def board_detail():
    id = request.args.get('id')
    print(id)
    return render_template('board_detail.html')