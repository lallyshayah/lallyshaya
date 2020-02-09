"""
Routes and views for the flask application.
"""

from datetime import datetime

from flask import render_template
from lallyflask import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/photoalbum')
def photoalbum():
    """Renders the photoalbum page."""
    return render_template(
        'photoalbum.html',
        title='photoalbum',
        year=datetime.now().year,
        message='photo album.'
    )

@app.route('/gridphotoalbum')
def gridphotoalbum():
    """Renders the gridphotoalbum page."""
    return render_template(
        'gridphotoalbum.html',
        title='gridphotoalbum',
        year=datetime.now().year,
        message='grid photo album.'
    )