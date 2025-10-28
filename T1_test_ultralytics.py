from ultralytics import YOLO

# 1. Load the Detection model (yolov8n.pt)
# This model only predicts bounding boxes and labels (no masks).
det_model = YOLO('T1_yolov8n.pt')

# 2. Define the local image path 
# Using the name of the image with the blue bus and people.
image_path = 'T1_blue_bus_street.jpg' 

# 3. Run Inference for Detection
print(f"Running Detection (Bounding Boxes only) on: {image_path}...")
# The 'save=True' option will save the output image in a new 'runs/detect/predict' folder.
det_results = det_model(image_path, conf=0.25, save=True)

# 4. Display results info and where to find the output
print(f"\n✅ Detection output generated. Check the 'runs/detect/predict' folder for the result.")
for r in det_results:
    # This will show the total number of bounding boxes detected.
    print(f"Detection - Total Boxes: {len(r.boxes)}")