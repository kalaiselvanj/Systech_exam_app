import cv2
import os
import datetime
import time
import numpy as np
import base64
from channels.generic.websocket import WebsocketConsumer

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

class WebcamConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        frame_data = base64.b64decode(text_data.split(',')[1])
        nparr = np.frombuffer(frame_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        print('hi')
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Draw a rectangle around each detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the number of faces detected
        cv2.putText(frame, ' ' + str(len(faces)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if len(faces) > 1:
            now = datetime.datetime.now()
            p = os.path.sep.join(['img', "More than one face detected{}.png".format(str(now).replace(":",''))])

            # Set the capture flag to True and save the image to the disk
            capture_flag = True
            cv2.imwrite(p, frame)
            img_counter += 1
            # Add a delay of 2 seconds if the capture flag is set to True
            if capture_flag:
                time.sleep(2)
                capture_flag = False

        if len(faces) == 0:
            now = datetime.datetime.now()
            p = os.path.sep.join(['img', "No face detected{}.png".format(str(now).replace(":",''))])

            # Set the capture flag to True and save the image to the disk
            capture_flag = True
            cv2.imwrite(p, frame)
            img_counter += 1
            # Add a delay of 2 seconds if the capture flag is set to True
            if capture_flag:
                time.sleep(2)
                capture_flag = False

        
        # Process the frame or perform any desired actions
        # For example, you can apply OpenCV operations or send the frame to an object detection model

        # Send the processed frame back to the client
        _, encoded_frame = cv2.imencode('.jpg', frame)
        self.send(encoded_frame.tobytes())
