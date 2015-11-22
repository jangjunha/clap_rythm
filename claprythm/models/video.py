# -*- coding: utf-8 -*-
from google.appengine.ext import db


class Video(db.Model):
    video_id = db.StringProperty()
    title = db.StringProperty()
    duration = db.IntegerProperty()
