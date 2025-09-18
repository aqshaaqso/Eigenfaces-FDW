import os
import cv2
import uuid

# Directory containing raw images for processing
raw_images_dir = "C:/work/fdw/unprocessed/"

# Directory to save cropped snapshots
snapshot_dir = "C:/work/fdw/snapshots/"
os.makedirs(snapshot_dir, exist_ok=True)

# Directory to move processed raw images
raw_pics_dir = "C:/work/fdw/raw_pics/"
os.makedirs(raw_pics_dir, exist_ok=True)

# Ensure the raw images directory exists
if not os.path.exists(raw_images_dir):
    raise FileNotFoundError(f"Raw images directory '{raw_images_dir}' does not exist.")

# Load the pre-trained face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Process each image in the raw images directory
for file in os.listdir(raw_images_dir):
    if file.endswith(".jpg") or file.endswith(".png"):
        img_path = os.path.join(raw_images_dir, file)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Failed to load image: {img_path}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cropped_face = img[y:y+h, x:x+w]
            random_name = f"{uuid.uuid4().hex}.jpg"
            snapshot_path = os.path.join(snapshot_dir, random_name)
            cv2.imwrite(snapshot_path, cropped_face)
            print(f"Cropped face saved as {snapshot_path}")

        # Assign a unique name to the original image and move it to the raw_pics folder
        unique_name = f"original_{uuid.uuid4().hex}.jpg"
        moved_path = os.path.join(raw_pics_dir, unique_name)
        os.rename(img_path, moved_path)
        print(f"Moved original image to {moved_path}")

print("Auto-cropping complete. Cropped images saved in the snapshots folder. Original images moved to the raw_pics folder with unique names.")