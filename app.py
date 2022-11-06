from flask import Flask
from flask import render_template
from flask import request

from PIL import Image

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["uploadFile"]
    img = Image.open(file)
    frame = Image.open("images/frame.png")

    resized_frame = frame.resize((img.width, img.height))

    img.paste(resized_frame, (0, 0), resized_frame)

    img.save("images/out.png")

    img.show()


if __name__ == "__main__":
    app.run(debug=True)
