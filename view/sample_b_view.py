from flask import render_template, request, redirect, session, url_for, flash
from model.sample_b import SampleB
from dao.sample_b_dao import SampleBDao
from sample import db, app
from view import session_view

sample_b_dao = SampleBDao(db)


@app.route('/createSampleB', methods=['POST', ])
def create_sample_b():
    text_field_a = request.form['text_field_b']
    id_field_a = request.form['id_field_a']

    sample_b = SampleB(text_field_a, id_field_a)
    sample_b_dao.save_sample_b(sample_b)

    return redirect(url_for('index'))


@app.route('/editSampleB/<int:id>')
def edit_sample_b(id_sample_b):
    if 'usuario_logado' not in session or session['logged_user'] is None:
        return redirect(url_for('login', next=url_for('edit_sample_b')))
    sample_b = sample_b_dao.search_by_id_sample_b(id_sample_b)
    return render_template('edit_sample_b.html', title='Editing Sample B', sample=sample_b)


@app.route('/refreshSampleB', methods=['POST', ])
def refresh_sample_b():
    text_field_a = request.form['text_field_b']
    id_field_a = request.form['id_field_a']
    sample_b = SampleB(text_field_a, id_field_a, id_field_b=request.form['id_field_b'])

    sample_b_dao.save_sample_b(sample_b)
    return redirect(url_for('index'))


@app.route('/deleteSampleB/<int:id>')
def delete_sample_b(id_field_b):
    sample_b_dao.delete_sample_b(id_field_b)
    flash('The example was successfully removed!')
    return redirect(url_for('index'))


@app.route('/newSampleB')
def new_sample_b():
    if 'logged_user' not in session or session['logged_user'] is None:
        return redirect(url_for('login', next=url_for('new_sample_b')))
    return render_template('new_sample_b.html', title='New Sample B')
