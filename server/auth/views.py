from .bp import auth
from db import User
from flask import request, redirect, render_template, session


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.find_by_username(username)
        if user and user.check_password(password):
            session['username'] = username
            return redirect('/')
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    if 'username' in session:
        session.clear()
        return redirect('/')
    return redirect('/auth/login')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.find_by_username(username)
        if user:
            return render_template('register.html', error='Username already taken')
        User.create(username, password)
        return redirect('/auth/login')
    return render_template('register.html')