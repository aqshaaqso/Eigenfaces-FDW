import os
import cv2
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Directory containing snapshots
snapshot_dir = "C:/work/fdw/snapshots/"

# Ensure the directory exists
if not os.path.exists(snapshot_dir):
    raise FileNotFoundError(f"Snapshot directory '{snapshot_dir}' does not exist.")

# Collect all snapshot images
snapshot_files = [f for f in os.listdir(snapshot_dir) if f.endswith(".jpg")]
if not snapshot_files:
    raise ValueError("No snapshot images found in the directory.")

# Load images and preprocess them
images = []
for file in snapshot_files:
    img_path = os.path.join(snapshot_dir, file)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Load as grayscale
    if img is None:
        raise ValueError(f"Failed to load image: {img_path}")
    resized_img = cv2.resize(img, (100, 100))  # Resize to 100x100 for consistency
    images.append(resized_img.flatten())  # Flatten the image

# Convert to numpy array
image_matrix = np.array(images)

# Train PCA for eigenfaces
n_components = min(len(snapshot_files), 50)  # Use up to 50 components or the number of images
pca = PCA(n_components=n_components, whiten=True)
pca.fit(image_matrix)

# Directory to save training results
train_results_dir = "C:/work/fdw/train_results/"
os.makedirs(train_results_dir, exist_ok=True)

# Save the PCA model and eigenfaces in the train_results directory
np.save(os.path.join(train_results_dir, "eigenfaces_components.npy"), pca.components_)
np.save(os.path.join(train_results_dir, "eigenfaces_mean.npy"), pca.mean_)

# Visualize and save the eigenfaces as images
eigenface_images_dir = os.path.join(train_results_dir, "eigenface_images")
os.makedirs(eigenface_images_dir, exist_ok=True)

# Save each eigenface as an image
for i, component in enumerate(pca.components_):
    eigenface = component.reshape(100, 100)  # Reshape to 100x100
    normalized_eigenface = cv2.normalize(eigenface, None, 0, 255, cv2.NORM_MINMAX)  # Normalize for visualization
    eigenface_path = os.path.join(eigenface_images_dir, f"eigenface_{i+1}.png")
    cv2.imwrite(eigenface_path, normalized_eigenface.astype(np.uint8))

    # Optionally display the eigenface
    plt.imshow(normalized_eigenface, cmap='gray')
    plt.title(f"Eigenface {i+1}")
    plt.axis('off')
    plt.show()

print(f"Eigenface training complete. Components and mean saved in '{train_results_dir}'.")
print(f"Eigenface images saved in '{eigenface_images_dir}'.")