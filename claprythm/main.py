# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, flash, url_for
from claprythm.models.note import Note
import json


blue_main = Blueprint('main', __name__, url_prefix='')


@blue_main.route('/')
def home():
    notes = [note for note in Note.all().order('-datetime').run(limit=6)]
    return render_template('index.html', notes=notes)


@blue_main.route('/test')
def test():
    return render_template('test.html')


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

    if notes == '' or notes == '[]':
        flash('Note is empty!')
        return redirect(url_for('main.video_create_note_form',
                                video_id=video_id))

    note = Note(video_id=video_id,
                title=title,
                writer_name=nickname,
                ip=request.remote_addr,
                notes=notes)
    note.put()

    flash('Created successfully!')
    return redirect(url_for('main.video_info', video_id=video_id))


@blue_main.route('/yt/<string:video_id>/random')
def video_play_random(video_id):
    note = {'video_id': video_id,
            'title': 'Random',
            'writer_name': 'Your Computer'}

    return render_template('play.html',
                           note=note,
                           random=True)


@blue_main.route('/play/<int:note_id>')
def play(note_id):
    note = Note.get_by_id(note_id)

    notes_o = []
    for t in json.loads(note.notes):
        notes_o.append({'t': t})

    return render_template('play.html',
                           note=note,
                           random=False,
                           notes_str=json.dumps(notes_o))


# Redirect
@blue_main.route('/watch')
def yt_watch():
    video_id = request.args.get('v', '')
    return redirect(url_for('main.video_info', video_id=video_id))
