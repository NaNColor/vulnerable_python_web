from flask import render_template, make_response, redirect, Flask, request, flash
from webapp import app
from models import UserModel
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/bruteforce', methods = ['POST', 'GET'])
def index_bruteforce():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        if not password or not username:
            flash(f'Error: filelds are required')
            return make_response(render_template('bruteforce.html',),200 )
        user = UserModel.find_by_username(username)
        if not user or not UserModel.verify_hash(password, user.password):
            flash(f'Error: Wrong username or password')
            return make_response(render_template('bruteforce.html',),200 )
        
        login_user(user, remember=True)
        return make_response(render_template('bruteforce_2.html',), 200)

    return make_response(render_template('bruteforce.html',), 200)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    #resp.set_cookie('sessionID', '', expires=0)
    return redirect("/bruteforce")
