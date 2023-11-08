import requests
from PIL import Image
from io import BytesIO
import face_recognition
import numpy as np

def getRawImg(compressed_img):
    image_stream = BytesIO(compressed_img)
    image = Image.open(image_stream)

    # Display the image (optional)
    image.show()

url = "https://res.cloudinary.com/dmp6f6f4h/image/upload/v1699420003/tznofd9jswitm5c0bi8k.jpg"  # Replace with the actual image URL

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:

    # Read the image content and create a PIL Image object
    image = Image.open(BytesIO(response.content))
    
    # Convert the PIL Image to a numpy array
    image_np = np.array(image)

    # Detect the faces
    face_locations = face_recognition.face_locations(image_np)
    print(f"Found {len(face_locations)} face(s) in the image.")

else:
    print("Failed to retrieve the image. Status code:", response.status_code)

