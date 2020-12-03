from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import json  
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './input'

@app.route('/')
def upload_f():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
      return 'ファイルのアップロードが完了しました。'

if __name__ == '__main__':
    app.run(debug = True)

