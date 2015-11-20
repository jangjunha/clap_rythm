# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect

blue_main = Blueprint('main', __name__, url_prefix='')


@blue_main.route('/yt/<string:video_id>')
def video_info(video_id):
    return render_template('video_info.html')


@blue_main.route('/watch')
def yt_watch():
    video_id = request.args.get('v', '')
    return redirect(url_for('main.video_info', video_id=video_id))
