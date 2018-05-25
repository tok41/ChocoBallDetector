import os
from flask import Flask, jsonify, request, render_template, send_file, abort
from werkzeug.utils import secure_filename

from chocoball_counter import ChocoballDetector

from io import BytesIO
from PIL import Image
import numpy as np


app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def root():
    return render_template('index.html')


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


@app.route('/chocoballimage', methods=['POST'])
def get_choco_image():
    if 'file' not in request.files:
        abort('No file part')
    file = request.files['file']
    if file.filename == '':
        abort('No selected file')
    cd = ChocoballDetector()
    res = cd.detectChocoballImage(file.stream)
    img_pil = Image.open(BytesIO(res['img']))
    img_pil.save('tmp/detected.png')
    return send_file('tmp/detected.png',
                     mimetype='image/png')


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


if __name__ == '__main__':
    app.debug = True
    app.run()
