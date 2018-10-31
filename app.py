import os
from flask import Flask, jsonify, request, render_template, send_file, abort, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from functools import wraps

from chocoball_counter import ChocoballDetector

from io import BytesIO
from PIL import Image
import numpy as np


# ----------- Global Variables -----------------
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
OUTPUT_FOLDER = './out'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif', 'JPG'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 3 * 5024 * 5024


def allowed_file(filename):
    """
    POSTされたファイルの拡張子チェック
    """
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# --------------- APIs -----------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chocoballimage', methods=['POST'])
def chocoball_image():
    # check input file
    if 'file' not in request.files:
        return render_template("index.html", err_text="No file part")
    img_file = request.files['file']
    if img_file and allowed_file(img_file.filename):
        filename = secure_filename(img_file.filename)
    else:
        return render_template("index.html", err_text="ファイルタイプエラー")
    if img_file.filename == '':
        return render_template("index.html", err_text="No selected file")
    # save input image
    raw_img_uri = os.path.join(UPLOAD_FOLDER, filename)
    img_file.save(raw_img_uri)
    # detect chocoball
    cd = ChocoballDetector()
    res = cd.detectChocoballImage(img_file.stream)
    cnt = (np.sum(res['objects'] == 0))
    # save detected image
    img_pil = Image.open(BytesIO(res['img']))
    img_uri = os.path.join(OUTPUT_FOLDER, 'res_' +
                           filename.rsplit('.', 1)[0]+'.png')
    img_pil.save(img_uri)
    return render_template("index.html", raw_img_file=raw_img_uri, out_img_file=img_uri, detected_number=cnt)


@app.route("/send", methods=['GET', 'POST'])
def send_image():
    if request.method == 'POST':
        img_file = request.files['file']

        # ファイルタイプチェック
        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
        else:
            return render_template("index.html", err_text="ファイルタイプエラー")

        # 画像ファイル保存
        raw_img_uri = os.path.join(UPLOAD_FOLDER, filename)
        img_file.save(raw_img_uri)
        return render_template("index.html", raw_img_file=raw_img_uri)
    else:
        return redirect(url_for('index'))


@app.route('/chocoball', methods=['POST'])
def chocoball():
    if 'file' not in request.files:
        abort('No file part')
    file = request.files['file']
    if file.filename == '':
        abort('No selected file')
    cd = ChocoballDetector()
    res = cd.detectChocoballImage(file.stream)
    cnt = float(np.sum(res['objects'] == 0))
    return jsonify({'num_chocoball': cnt})


@app.route('/chocoball2', methods=['POST'])
def chocoball2():
    """
    for debug
    """
    if 'file' not in request.files:
        abort('No file part')
    file = request.files['file']
    if file.filename == '':
        abort('No selected file')
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    result = {'count': 3}
    return jsonify(result)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/out/<filename>')
def output_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)


# ---------------- MAIN ----------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
