from flask import Blueprint, url_for, render_template

from application import db

landing_app = Blueprint('landing_app', __name__)

@landing_app.route('/')
def init():
    return render_template("landing/landing_newsletter.html")
