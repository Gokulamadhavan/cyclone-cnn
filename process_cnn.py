import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from PIL import Image
import glob
import os

# Parameters
IMAGE_SIZE = (128, 128)  # Resize images for faster prototyping
BATCH_SIZE = 2

# Load and preprocess images
def load_images(image_folder):
    images = []
    image_paths = glob.glob(os.path.join(image_folder, '*.jpg'))
    for img_path in image_paths:
        img = Image.open(img_path).convert('L')  # convert to grayscale
        img = img.resize(IMAGE_SIZE)
        img_array = np.array(img) / 255.0  # normalize to [0,1]
        images.append(img_array)
    images = np.array(images)
    images = images[..., np.newaxis]  # add channel dimension
    return images

# Example folder path
image_folder = 'path_to_your_downloaded_images'

# Load images
X = load_images(image_folder)
print(f"Loaded {X.shape[0]} images.")

# Dummy labels for testing (just zeros)
y = np.zeros((X.shape[0], 1))

# Build a simple CNN model
model = models.Sequential([
    layers.Input(shape=(*IMAGE_SIZE, 1)),
    layers.Conv2D(16, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, (3,3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # example output
])

model.compile(optimizer='adam', loss='binary_crossentropy')

# Train briefly just to test pipeline
model.fit(X, y, epochs=3, batch_size=BATCH_SIZE)

print("Test run complete!")
