from flask import ( Blueprint, render_template)

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/')
def fact():
    return render_template('fact.html')

@bp.route('/newfact')
def newfact():
    return render_template('newfact.html')  