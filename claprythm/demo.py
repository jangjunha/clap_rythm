# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request

blue_demo = Blueprint('demo', __name__, url_prefix='/demo')


@blue_demo.route('/')
def home():
    return render_template('demo.html')
