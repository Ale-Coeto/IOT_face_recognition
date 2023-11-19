import base64
from PIL import Image
from io import BytesIO
import requests
import face_recognition
import numpy as np
# from flask import jsonify

def getBase64Image(compressed_img):
    # Decode the base64 string into bytes
    image_bytes = base64.b64decode(compressed_img)

    # Open the image using Pillow
    image = Image.open(BytesIO(image_bytes))
    image_np = np.array(image)

    image.show()
    return image_np
    # Display or save the image as needed

def getURLImage(url):
    # print("url: ", url)
    response = requests.get(url)
    if response.status_code == 200:
        # Read the image content and create a PIL Image object
        image = Image.open(BytesIO(response.content))
        image_np = np.array(image)
        # image.show()  # Display the image (you can remove this line if you don't want to display it)
        return image_np
    
    return None
    # else:
    #     print("Failed to retrieve the image. Status code:", response.status_code)

def recognize_faces(raw_image, images):

    try:
        # Decode raw image
        base64_image = getBase64Image(raw_image)

        # Get images by url
        imgs = []
        # names = []
        # print(images)
        for image in images:
            # print(image)
            url = image['url']
            name = image['name']
            # print(url, "name: ", name)
            imgs.append([getURLImage(url),name])
            # names.append(name)

        # Detect the faces
        base_encodings = face_recognition.face_encodings(base64_image)[0]

        for imageObj in imgs:
            image = imageObj[0]
            
            encodings = face_recognition.face_encodings(image)[0]
            if len(encodings) == 0:
                return False
            
            results = face_recognition.compare_faces([base_encodings], encodings, 0.62)
            if True in results:
                # print(results)
                print("result: " , imageObj[1])
                return imageObj[1]
        
        print("none")
        return "None"
    
    except Exception as e:
        print(e)
        return "error"

#TEST
# urls = [
#     "https://res.cloudinary.com/dmp6f6f4h/image/upload/v1699420003/tznofd9jswitm5c0bi8k.jpg",  # Replace with the actual image URL,
#     "https://res.cloudinary.com/dmp6f6f4h/image/upload/v1689564122/samples/smile.jpg"
# ]     
# raw = "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"

# recognize(raw, urls)
