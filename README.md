# Face detection and recognition

## Face Detection
Using an OpenMV camera, images were analyzed to find faces. If a detection was found, the image was sent as base64 to a NodeMCU through UART. This was programmed using micro-python and the OpenMV IDE.

## Face Recognition
For the recognition process, an API was developed using Flask to recieve the image in base64 and the urls of the images to compare. Then, after decoding the images, the face_recognition library was used to compare the encodings of the faces and return the name of the person in the image if found. The API was hosted in an AWS EC2 instance using docker.
