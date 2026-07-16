from flask import Blueprint
from flask import render_template

user = Blueprint('user', __name__)

@user.route('/user_account')
def user_account():
    return render_template('main/user.html')