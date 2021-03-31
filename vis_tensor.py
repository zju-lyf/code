import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import cv2
def visualize_tensor(input,dir):
    input = input.transpose(0,1)
    input = input.transpose(1,2)
    transform1 = transforms.ToPILImage(mode='RGB')
    image = transform1(np.uint8(input.numpy()))
    image.save(dir)

