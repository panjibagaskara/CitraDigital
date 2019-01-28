import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_folder='gambar')

app_root = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def uploadimage():
    target = os.path.join(app_root, 'gambar/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("gambar"):
        print(file)
        nama = file.filename
        tujuan = "/".join([target, nama])
        print(tujuan)
        file.save(tujuan)
    return render_template('index.html',filename=nama)

if __name__ == "__main__":
    app.run(debug=True)