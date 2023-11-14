from flask import Flask, request, jsonify
from recognize import recognize_faces

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get('/')
def hello_world():
    return "Hello, World!"

@app.route('/getImg', methods=['POST'])
def get_img():
    input = request.get_json()["img"]
    
    return jsonify({"result": input})


@app.route('/recognize', methods=['POST'])
def recognize():
    raw_image = request.get_json()["img"]
    images = request.get_json()["images"]
    # getBase64Image(raw_image)
    # result = getURLImage(images[0])
    result = recognize_faces(raw_image, images)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=80)