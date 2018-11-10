from flask import render_template, request, redirect, session, flash, url_for
from dao.session_user_dao import SessionUserDao
from sample import db, app

session_user_dao = SessionUserDao(db)


@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)


@app.route('/authenticate', methods=['POST', ])
def authenticate():
    session_user = session_user_dao.search_by_id(request.form['username'])
    if session_user:
        if session_user.password == request.form['password']:
            session['logged_user'] = session_user.username
            flash(session_user.name + ' Successfully logged in!')
            next_page = request.form['next']
            return redirect(next_page)
    else:
        flash('not logged in, try again!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('No user logged in!')
    return redirect(url_for('index'))
