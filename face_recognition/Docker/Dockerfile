FROM animcogn/face_recognition:cpu-latest


EXPOSE 8000

# RUN cd /app && pip3 install -r requirements.txt
# RUN cd /app && python3 app.py
# Mount relative to the current working directory

COPY ../. /app
WORKDIR /app
RUN pip3 install -r requirements.txt

