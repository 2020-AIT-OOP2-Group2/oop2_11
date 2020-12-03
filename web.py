from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import json
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './input'


@app.route('/')
def upload_f():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'ファイルのアップロードが完了しました。'


@app.route('/original', methods=["GET"])
def original_list():
    base_dir = 'input'
    app.static_folder = base_dir
    image_paths = os.listdir("./"+base_dir+"/")
    image_type = 'Original'

    return render_template("img_list.html", image_type=image_type, image_paths=image_paths)


@app.route('/grayscale', methods=["GET"])
def grayscale_list():
    base_dir = 'output_grayscale'
    app.static_folder = base_dir
    image_paths = os.listdir("./"+base_dir+"/")
    image_type = 'Grayscale'

    return render_template("img_list.html", image_type=image_type, image_paths=image_paths)


@app.route('/canny', methods=["GET"])
def canny_list():
    base_dir = 'output_canny'
    app.static_folder = base_dir
    image_paths = os.listdir("./"+base_dir+"/")
    image_type = 'Canny'

    return render_template("img_list.html", image_type=image_type, image_paths=image_paths)


@app.route('/face', methods=["GET"])
def face_list():
    base_dir = 'input'
    app.static_folder = base_dir
    image_paths = os.listdir("./"+base_dir+"/")
    image_type = 'Face'

    return render_template("img_list.html", image_type=image_type, image_paths=image_paths)


if __name__ == '__main__':
    app.run(debug=True)
