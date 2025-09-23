"""
Simple Object Classifier for Cropped Detections
"""
import torch
from torchvision import models, transforms

class ObjectClassifier:
    def __init__(self, num_classes=3, weights_path='models/classification/mobilenetv2.pth'):
        self.model = models.mobilenet_v2(pretrained=False)
        self.model.classifier[1] = torch.nn.Linear(self.model.last_channel, num_classes)
        self.model.load_state_dict(torch.load(weights_path, map_location='cpu'))
        self.model.eval()

    def classify(self, image_crop):
        preprocess = transforms.Compose([
            transforms.Resize((128,128)),
            transforms.ToTensor(),
            transforms.Normalize([0.485,0.456,0.406], [0.229,0.224,0.225])
        ])
        with torch.no_grad():
            input_tensor = preprocess(image_crop).unsqueeze(0)
            preds = self.model(input_tensor)
        return torch.argmax(preds, dim=1).item()
