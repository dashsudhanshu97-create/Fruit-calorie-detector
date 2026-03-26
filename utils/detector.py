from ultralytics import YOLO
from collections import Counter

model = YOLO("yolov8n.pt")

def detect_fruits(image):
    results = model.predict(image, conf=0.4)

    if results[0].boxes is None:
        return {}

    labels = results[0].boxes.cls.tolist()
    names = model.names

    detected = [names[int(i)] for i in labels]
    return Counter(detected)
