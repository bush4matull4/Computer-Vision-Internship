# T3_detect_objects.py
# Task: Detect objects in extracted frames using YOLOv8

from ultralytics import YOLO
import os
import glob

# --- Paths ---
INPUT_DIR = 'T3_input_frames/'
OUTPUT_DIR = 'T3_output_processed/'

# --- Load YOLO model ---
model = YOLO('yolov8n.pt')  # you can also use yolov8s.pt or yolov8x.pt

# --- Ensure output folder exists ---
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Process all frames ---
for img_path in glob.glob(os.path.join(INPUT_DIR, '*.jpg')):
    results = model(img_path)
    results[0].save(filename=os.path.join(OUTPUT_DIR, os.path.basename(img_path)))

print("✅ Object Detection Completed! Check the 'T3_output_processed' folder.")
