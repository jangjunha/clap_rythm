# -*- coding: utf-8 -*-
from google.appengine.ext import db
from claprythm.models.user import User


class Note(db.Model):
    video_id = db.StringProperty()
    video_title = db.StringProperty()
    notes = db.TextProperty()
    title = db.StringProperty()

    writer = db.ReferenceProperty(User)
    writer_name = db.StringProperty()       # Not registered
    ip = db.StringProperty()

    datetime = db.DateTimeProperty(auto_now_add=True)
