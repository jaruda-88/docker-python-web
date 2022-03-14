from flask import Blueprint, redirect, render_template, request

bp = Blueprint("login", __name__, url_prefix='/login')


@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print("dd")
        return render_template('login.html')
    else:
        print("ddd")
        return render_template('login.html')


@bp.route('/register')
def register():
    print("ddddddddddd")
    return render_template('register_user.html')
