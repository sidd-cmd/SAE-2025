"""
YOLOv8 2D Object Detection Pipeline for Drone Perception
"""
import cv2
from ultralytics import YOLO

class YoloDetector:
    def __init__(self, model_path='models/yolo/weights/yolov8n.pt'):
        self.model = YOLO(model_path)

    def detect(self, image):
        results = self.model(image)
        return results[0].boxes.xyxy, results[0].probs

if __name__ == "__main__":
    detector = YoloDetector()
    frame = cv2.imread('test.jpg')
    boxes, probs = detector.detect(frame)
    print("Detected boxes:", boxes)
