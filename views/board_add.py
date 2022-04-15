from flask import Blueprint, render_template, request
import requests
import json


bp = Blueprint('board_add', __name__, url_prefix='/board_add')

@bp.route('/')
def board():
    return render_template('board_add.html')