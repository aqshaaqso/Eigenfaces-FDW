from flask import Flask, Response, render_template, send_file
import cv2
import os
import numpy as np
import logging

app = Flask(__name__)

# Load the pre-trained face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the camera
camera = cv2.VideoCapture(0)

# Ensure the snapshot directory path is correctly set to 'C:/work/unprocessed'
snapshot_dir = "C:/work/fdw/unprocessed"
os.makedirs(snapshot_dir, exist_ok=True)

logging.basicConfig(level=logging.DEBUG)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Encode the frame as a JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame as a byte stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/snapshot_original')
def snapshot_original():
    """Take a snapshot of the original video feed without detection rectangles."""
    try:
        success, frame = camera.read()
        if not success:
            logging.error("Failed to read from camera")
            return {"error": "Failed to capture snapshot"}, 500

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Generate a sequential filename
        existing_files = [f for f in os.listdir(snapshot_dir) if f.startswith("ss") and f.endswith(".jpg")]
        next_index = len(existing_files) + 1
        snapshot_filename = f"ss{next_index}.jpg"
        snapshot_path = os.path.join(snapshot_dir, snapshot_filename)

        cv2.imwrite(snapshot_path, frame)  # Save the full frame without rectangles
        logging.info(f"Snapshot saved at {snapshot_path}")
        return send_file(snapshot_path, mimetype='image/jpeg')
    except cv2.error as e:
        logging.exception("OpenCV error in snapshot_original")
        return {"error": "OpenCV error occurred", "details": str(e)}, 500
    except Exception as e:
        logging.exception("Unexpected error in snapshot_original")
        return {"error": "Internal Server Error", "details": str(e)}, 500

@app.route('/snapshot_eigenfaces')
def snapshot_eigenfaces():
    return {"error": "This feature has been removed."}, 410

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)