from flask import render_template
from . import root

@root.route('/')
def index():
    title = 'Pitches Home'
    return render_template('index.html', title=title)

