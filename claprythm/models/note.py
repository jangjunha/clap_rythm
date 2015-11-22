# -*- coding: utf-8 -*-
from google.appengine.ext import db
from claprythm.models.user import User


class Note(db.Model):
    video_id = db.StringProperty()
    notes = db.StringProperty()
    title = db.StringProperty()

    writer = db.ReferenceProperty(User)
    writer_name = db.StringProperty()       # Not registered
    ip = db.StringProperty()

    datetime = db.DateTimeProperty()
