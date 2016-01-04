# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, flash, \
    url_for, abort
from claprythm.models.note import Note
import json


blue_main = Blueprint('main', __name__, url_prefix='')


@blue_main.route('/')
def home():
    notes = [note for note in Note.all().order('-datetime').run(limit=16)]
    return render_template('index.html', notes=notes)


@blue_main.route('/test')
def test():
    return render_template('create_tmp.html')


@blue_main.route('/close_popup')
def close_popup():
    return render_template('close_popup.html')


@blue_main.route('/yt/<string:video_id>')
def video_info(video_id):
    notes = [note for note in Note.all().filter('video_id =', video_id)]
    return render_template('video_info.html', video_id=video_id, notes=notes)


@blue_main.route('/yt/<string:video_id>/create', methods=['GET'])
def video_create_note_form(video_id):
    return render_template('video_create_note.html', video_id=video_id)


@blue_main.route('/yt/<string:video_id>/create', methods=['POST'])
def video_create_note(video_id):
    title = request.form.get('title', 'Noname')
    nickname = request.form.get('nickname', 'Anonymous')
    notes = request.form.get('notes', '')
    video_title = request.form.get('video_title', 'UNTITLED')

    if notes == '' or notes == '[]':
        flash('Note is empty!')
        return redirect(url_for('main.video_create_note_form',
                                video_id=video_id))

    note = Note(video_id=video_id,
                video_title=video_title,
                title=title,
                writer_name=nickname,
                ip=request.remote_addr,
                notes=notes)
    note.put()

    flash('Created successfully!')
    return redirect(url_for('main.video_info', video_id=video_id))


@blue_main.route('/yt/<string:video_id>/note/random')
def video_note_random(video_id):
    note = {'video_id': video_id,
            'title': 'Random',
            'writer_name': 'Your Computer'}

    return render_template('note_info.html',
                           note=note,
                           random=True,
                           args=request.args)


@blue_main.route('/yt/<string:video_id>/note/<int:note_id>')
def video_note(video_id, note_id):
    note = Note.get_by_id(note_id)

    if note.video_id != video_id:
        return abort(400)

    return render_template('note_info.html',
                           note=note,
                           random=False,
                           args=request.args)


@blue_main.route('/yt/<string:video_id>/play/random', methods=['POST', 'GET'])
def video_play_random(video_id):
    clap_range = request.form.get('range-result', 50000)
    if clap_range == '' or int(clap_range) == 0:
        clap_range = 50000
    elif clap_range < 20000:
        clap_range = 20000
    else:
        clap_range = int(clap_range)

    note = {'video_id': video_id,
            'title': 'Random',
            'writer_name': 'Your Computer'}

    return render_template('play.html',
                           note=note,
                           clap_range=clap_range,
                           random=True)


@blue_main.route('/yt/<string:video_id>/play/<int:note_id>',
                 methods=['POST', 'GET'])
def video_play(video_id, note_id):
    note = Note.get_by_id(note_id)

    if note.video_id != video_id:
        return abort(400)

    clap_range = request.form.get('range-result', 50000)
    if clap_range == '' or int(clap_range) == 0:
        clap_range = 50000
    elif clap_range < 20000:
        clap_range = 20000
    else:
        clap_range = int(clap_range)

    notes_o = []
    for t in json.loads(note.notes):
        notes_o.append({'t': t})

    return render_template('play.html',
                           note=note,
                           clap_range=clap_range,
                           random=False,
                           notes_str=json.dumps(notes_o))


# Redirect
@blue_main.route('/watch')
def yt_watch():
    video_id = request.args.get('v', '')
    return redirect(url_for('main.video_info', video_id=video_id))
