"""
Monocular Depth Estimation using MiDaS Model
"""
import torch
import cv2
from torchvision.transforms import Compose, Resize, ToTensor, Normalize

class DepthEstimator:
    def __init__(self, midas_path='models/depth_estimation/midas.pth'):
        self.model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
        self.model.load_state_dict(torch.load(midas_path, map_location='cpu'))
        self.model.eval()
        self.transform = Compose([
            Resize((256, 256)),
            ToTensor(),
            Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

    def estimate(self, image):
        input_tensor = self.transform(image).unsqueeze(0)
        with torch.no_grad():
            depth = self.model(input_tensor)
        return depth.squeeze().cpu().numpy()
