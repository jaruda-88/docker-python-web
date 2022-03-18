from flask import Blueprint, redirect, render_template, request

bp = Blueprint("login", __name__, url_prefix='/login')


@bp.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@bp.route('/register')
def register():
    return render_template('register_user.html')
