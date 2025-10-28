<<<<<<< HEAD
# multi_img_seg.py
# Task 2: Multiple Image Object Detection & Segmentation
# Author: Bushra Amatulla

from ultralytics import YOLO
import os
import glob 

# --- Configuration ---
IMAGE_DIR = 'images/' 

# MODEL CHANGE: Ab hum Object Detection ke liye 'yolov8x.pt' use karenge
MODEL_NAME = 'yolov8x.pt' 

# --- Automatic Image Path Finding (Wahi Code) ---
search_path = os.path.join(IMAGE_DIR, '*') 
all_files = glob.glob(search_path) 
IMAGE_PATHS = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if len(IMAGE_PATHS) < 3:
    print(f"🛑 ERROR: '{IMAGE_DIR}' folder mein sirf {len(IMAGE_PATHS)} image files mili. Kam se kam 3 chahiye.")
    print(f"Mili hui files: {[os.path.basename(p) for p in IMAGE_PATHS]}")
    exit() 

print(f"Found {len(IMAGE_PATHS)} images to process for DETECTION: {', '.join([os.path.basename(p) for p in IMAGE_PATHS])}")

# --- Model Loading aur Prediction ---
print(f"Loading model: {MODEL_NAME}...")
# Note: Agar 'yolov8x.pt' pehle download nahi hua hai, toh woh yahan download hoga.
model = YOLO(MODEL_NAME) 

print("Running DETECTION predictions...")

# Predictions chalaein (Object Detection ke liye)
results = model(
    source=IMAGE_PATHS, 
    save=True,  # Processed images runs/detect/predict mein save ho jayengi
    conf=0.25 
)

# --- Results Verification ---
print("\n--- Results Summary (Detection) ---")
for result in results:
    filename = os.path.basename(result.path) 
    # Boxes (Detection) ki sankhya check karein
    num_boxes = len(result.boxes)
    
    print(f"File: {filename}")
    print(f"  Total Objects Detected (Bounding Boxes): {num_boxes}")

# Output folder ka naam (Detect mode ke liye 'detect' hoga)
output_folder = 'runs/detect/predict'
    
=======
# multi_img_seg.py
# Task 2: Multiple Image Object Detection & Segmentation
# Author: Bushra Amatulla

from ultralytics import YOLO
import os
import glob 

# --- Configuration ---
IMAGE_DIR = 'images/' 

# MODEL CHANGE: Ab hum Object Detection ke liye 'yolov8x.pt' use karenge
MODEL_NAME = 'yolov8x.pt' 

# --- Automatic Image Path Finding (Wahi Code) ---
search_path = os.path.join(IMAGE_DIR, '*') 
all_files = glob.glob(search_path) 
IMAGE_PATHS = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if len(IMAGE_PATHS) < 3:
    print(f"🛑 ERROR: '{IMAGE_DIR}' folder mein sirf {len(IMAGE_PATHS)} image files mili. Kam se kam 3 chahiye.")
    print(f"Mili hui files: {[os.path.basename(p) for p in IMAGE_PATHS]}")
    exit() 

print(f"Found {len(IMAGE_PATHS)} images to process for DETECTION: {', '.join([os.path.basename(p) for p in IMAGE_PATHS])}")

# --- Model Loading aur Prediction ---
print(f"Loading model: {MODEL_NAME}...")
# Note: Agar 'yolov8x.pt' pehle download nahi hua hai, toh woh yahan download hoga.
model = YOLO(MODEL_NAME) 

print("Running DETECTION predictions...")

# Predictions chalaein (Object Detection ke liye)
results = model(
    source=IMAGE_PATHS, 
    save=True,  # Processed images runs/detect/predict mein save ho jayengi
    conf=0.25 
)

# --- Results Verification ---
print("\n--- Results Summary (Detection) ---")
for result in results:
    filename = os.path.basename(result.path) 
    # Boxes (Detection) ki sankhya check karein
    num_boxes = len(result.boxes)
    
    print(f"File: {filename}")
    print(f"  Total Objects Detected (Bounding Boxes): {num_boxes}")

# Output folder ka naam (Detect mode ke liye 'detect' hoga)
output_folder = 'runs/detect/predict'
    
>>>>>>> a0ebff8413f221b09af6c92cf22bfa413d28abaa
print(f"\n✅ Object Detection Task complete. Processed images output folder: {output_folder}")