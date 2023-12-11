from markupsafe import escape
from flask import render_template, make_response, redirect, Flask, request, flash
from webapp import app
from models import UserModel
from flask_login import login_required, current_user


@app.route("/idor")
@login_required
def redirect_to_page():
    found_id = (UserModel.find_by_username(current_user.username)).id
    # находим в бд пользователя текущей сессии и переходим на страницу с его id
    return redirect('/idor/'+str(found_id))

@app.route("/idor/<id>")
@login_required
def index_idor(id):
    #username = current_user.username

    user = UserModel.find_by_id(escape(id))

    return make_response(render_template('idor.html', secret=user.secret, username = user.username), 200)