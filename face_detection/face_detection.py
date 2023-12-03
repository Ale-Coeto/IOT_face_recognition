
import sensor, time, image
import pyb
from pyb import UART
import ubinascii


# Reset sensor
sensor.reset()

# Sensor settings
sensor.set_contrast(3)
sensor.set_gainceiling(16)
# HQVGA and GRAYSCALE are the best for face tracking.
sensor.set_framesize(sensor.HQVGA)
sensor.set_pixformat(sensor.RGB565)


# Load Haar Cascade
# By default this will use all stages, lower satges is faster but less accurate.
face_cascade = image.HaarCascade("frontalface", stages=25)
#print(face_cascade)

# FPS clock
clock = time.clock()

green_led = pyb.LED(2)
uart = UART(3, 115200, timeout_char=0)


counter = 0

while (True):
    clock.tick()

    # Capturar la imagen
    img = sensor.snapshot()

    # Detecar rostros
    objects = img.find_features(face_cascade, threshold=0.79, scale_factor=1.25)

    # Si se encontró un rostro, se buscar que la cara cumpla con un área
    if len(objects) > 0:
        face = objects[0]
        area = face[2] * face[3]

        # Si el área es adecuada, se suma un contador
        if area > 10000:
            green_led.on()
            img.draw_rectangle(face)
            counter = counter + 1

    else:
        green_led.off()
        counter = 0

    # Si el contador es igual a 1,
    if counter == 1:

        image_bytes = img.compress(quality=30).bytearray()
        img_base64 = ubinascii.b2a_base64(image_bytes)

        res = img_base64
        uart.write(f"{res}\n")
        print(img_base64)


