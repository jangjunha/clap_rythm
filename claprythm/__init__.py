# -*- coding: utf-8 -*-
from flask import Flask
import logging


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from claprythm.demo import blue_demo
    from claprythm.main import blue_main

    app.register_blueprint(blue_demo)
    app.register_blueprint(blue_main)

    return app
