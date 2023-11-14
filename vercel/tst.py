from PIL import Image, ImageDraw
import io

# Create a new image with a white background
width, height = 200, 200  # Adjust the size as needed
image = Image.new("RGB", (width, height), "white")

# Create a drawing context
draw = ImageDraw.Draw(image)

# Draw a red rectangle (adjust the coordinates and dimensions as needed)
left_top = (50, 50)
right_bottom = (150, 150)
red = (255, 0, 0)  # RGB color for red
draw.rectangle([left_top, right_bottom], fill=red)

# Convert the image to a byte array (string)
img_byte_array = io.BytesIO()
image.save(img_byte_array, format='PNG')  # You can choose the desired format

# Get the byte array content as a string
byte_array_content = img_byte_array.getvalue()

# Close the image
image.close()

# Close the byte array (recommended after you're done with it)
img_byte_array.close()

from io import BytesIO 
import face_recognition
import numpy as np

# compressed_image_data = b'\x89PNG\r\n\x00\x00'
compressed_image_data = byte_array_content
print(byte_array_content)
# Create a BytesIO object and load the image
image_stream = BytesIO(compressed_image_data)
image = Image.open(image_stream)
image_np = np.array(image)

# Detect the faces
face_locations = face_recognition.face_locations(image_np)
print(f"Found {len(face_locations)} face(s) in the image.")

# Display the image (optional)
image.show()