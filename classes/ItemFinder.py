from classes.ImageProcessor import ImageProcessor
from classes.Item import Item

import cv2
import numpy as np

class ItemFinder:
    @staticmethod
    def find_matches(inventory_gray, item_data, threshold=0.8):
        image = ImageProcessor.load_image(f'./items/{item_data["name"]}.png', grayscale=True)
        result = cv2.matchTemplate(inventory_gray, image, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)
        matches = []
        for pt in zip(*locations[::-1]):
            matches.append(Item(item_data, pt))
        return matches