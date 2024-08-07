from flask import Flask, request, jsonify
from Utils.recognize import recognize_faces


app = Flask(__name__)

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
    result = recognize_faces(raw_image, images)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
