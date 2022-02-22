# main.py

from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/vote', methods=['POST'])
def vote():
    return redirect("http://www.google.com", code=302)


@main.route('/db', methods=['POST'])
def db():
    return render_template('db.html')
