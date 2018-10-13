import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, abort
import json
import glob
import re

app = Flask(__name__)
conf = {}

for filename in glob.glob('conf/*.json'):
    matches = re.findall('conf/(\d\d\d\d)\.json', filename)
    if len(matches) > 0:
        year = matches[0]
        with open(filename) as f:
            conf[year] = json.load(f)

photos = []
for filename in glob.glob('photos/*.JPG'):
    photos.append("/" + filename)

def valid_id(year, unique_id):
    if year in conf and unique_id in conf[year]:
        return True
    return False

@app.route('/')
def hello_world():
    return 'Hello, World! From luke.'

@app.route('/reveal/<int:year_raw>/<string:unique_id>')
def show_user_profile(year_raw, unique_id):
    year = str(year_raw)
    if valid_id(year, unique_id):
        return render_template('{}/reveal.html'.format(year), info=conf[year][unique_id], photos=photos)
    abort(404)
    #return redirect('/')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/photos/<path:path>')
def send_photos(path):
    return send_from_directory('photos', path)
