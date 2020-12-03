from flask import Flask, request, render_template, url_for
import os

app = Flask(__name__)


@app.route('/original', methods=["GET"])
def image_list():
    base_dir = 'input'
    app.static_folder = base_dir
    image_paths = os.listdir("./"+base_dir+"/")
    image_type = 'Original'

    return render_template("img_list.html", image_type=image_type, image_paths=image_paths)


if __name__ == '__main__':
    app.run(debug=True)
