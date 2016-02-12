from flask import request, redirect
from claprythm import create_app

app = create_app('claprythm_config')

@app.before_request
def before_request():
    if request.host.endswith('clap-rythm.appspot.com'):
        return redirect('https://clap.heek.kr')

