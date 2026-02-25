
import requests
from datetime import datetime
import os

# Get the folder where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Example: saving output folder inside cnn
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Example of saving a file inside that folder
file_path = os.path.join(OUTPUT_DIR, "result.txt")
with open(file_path, "w") as f:
    f.write("Hello, CNN folder!")

print(f"Saved file at: {file_path}")

import sys
with open(r"C:/Users/HP/cnn/tasklog.txt", "a") as f:
    f.write(f"Running test.py from {os.getcwd()}\n")
    f.write(f"Python executable: {sys.executable}\n")

# Save folder
save_dir = r"C:/Users/HP/cnn/satellite_images"
os.makedirs(save_dir, exist_ok=True)


# Image URLs
image_urls = {
    "IR": "https://mausam.imd.gov.in/Satellite/3Dasiasec_ir1.jpg",
    "VIS": "https://mausam.imd.gov.in/Satellite/3Dasiasec_vis.jpg",
    "WV": "https://mausam.imd.gov.in/Satellite/3Dasiasec_wv.jpg",
}

# Timestamp for unique filenames
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

for key, url in image_urls.items():
    with open(r"C:/Users/HP/cnn/tasklog.txt", "a") as log:
        log.write(f"Starting download for {key} at {datetime.now()}\n")


    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        filename = f"{key}_{timestamp}.jpg"
        filepath = os.path.join(save_dir, filename)

        with open(filepath, "wb") as img_file:
            img_file.write(response.content)

        # Log the full absolute path
        with open(r"C:/Users/HP/cnn/tasklog.txt", "a") as log:
            log.write(f"Saved {key} to: {os.path.abspath(filepath)}\n")

        print(f"✅ Saved {key} as {filename}")

    except Exception as e:
        print(f"❌ Failed to download {key}: {e}")

print("Done.")
with open(r"C:/Users/HP/cnn/tasklog.txt", "a") as log:
    log.write("=== Script finished ===\n")

