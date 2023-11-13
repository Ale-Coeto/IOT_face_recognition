from flask import Flask, request, jsonify
from api.recognize import recognize_faces
import base64
from PIL import Image
from io import BytesIO
import requests
import face_recognition
import numpy as np

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
    result = recognize_faces(raw_image, images)

    return jsonify({"result": result})

# def getBase64Image(compressed_img):
#     # Decode the base64 string into bytes
#     image_bytes = base64.b64decode(compressed_img)

#     # Open the image using Pillow
#     image = Image.open(BytesIO(image_bytes))
#     image_np = np.array(image)

#     # image.show()
#     return image_np
#     # Display or save the image as needed

# def getURLImage(url):
#     # print("url: ", url)
#     response = requests.get(url)
#     if response.status_code == 200:
#         # Read the image content and create a PIL Image object
#         image = Image.open(BytesIO(response.content))
#         image_np = np.array(image)
#         # image.show()  # Display the image (you can remove this line if you don't want to display it)
#         return image_np
    
#     return None
#     # else:
#     #     print("Failed to retrieve the image. Status code:", response.status_code)

# def recognize_faces(raw_image, images):

#     try:
#         # Decode raw image
#         base64_image = getBase64Image(raw_image)

#         # Get images by url
#         imgs = []
#         # print(images)
#         for url in images:
#             # print(url)
#             imgs.append(getURLImage(url))

#         # Detect the faces
        
#         base_encodings = face_recognition.face_encodings(base64_image)[0]

#         for image in imgs:
#             encodings = face_recognition.face_encodings(image)[0]
#             if len(encodings) == 0:
#                 return False
            
#             results = face_recognition.compare_faces([base_encodings], encodings)
#             if True in results:
#                 # print(results)
#                 # print(True)
#                 return True
        
#         # print(False)
#         return False
    
#     except Exception as e:
#         print(e)
#         return False
