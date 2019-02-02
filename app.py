import os
import fungsi
from flask import Flask, render_template, request, url_for, make_response
from shutil import copyfile
from functools import wraps, update_wrapper
from datetime import datetime

app = Flask(__name__, static_folder='gambar')

app_root = os.path.dirname(os.path.abspath(__file__))

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
        
    return update_wrapper(no_cache, view)

@app.route("/")
def index():
    return render_template('index.html')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/upload', methods=['POST'])
def uploadimage():
    target = os.path.join(app_root, 'gambar/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("gambar"):
        print(file)
        nama = "img_process.jpg"
        tujuan = "/".join([target, nama])
        print(tujuan)
        file.save(tujuan)
        copyfile("gambar/img_process.jpg","gambar/img_process_normal.jpg")
    return render_template('index.html',filename=nama)

@app.route('/grayscale', methods=['POST'])
def grayscaleimage():
    fungsi.grayscale()
    return render_template('index.html', filename='img_process.jpg')

if __name__ == "__main__":
    app.run(debug=True)