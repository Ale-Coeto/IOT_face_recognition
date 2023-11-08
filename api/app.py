from flask import Flask, request, jsonify
import face_recognition
import requests
from PIL import Image
from io import BytesIO

# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

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

    # Send an HTTP GET request to the URL
    for img in images:
        url = img

        response = requests.get(url)

        if response.status_code == 200:
            # Read the image content and create a PIL Image object
            image = Image.open(BytesIO(response.content))
            image.show()  # Display the image (you can remove this line if you don't want to display it)
    else:
        print("Failed to retrieve the image. Status code:", response.status_code)

    
    return jsonify({"result": input})

