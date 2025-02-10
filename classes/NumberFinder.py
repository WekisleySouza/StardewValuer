from classes.ImageProcessor import ImageProcessor
from classes.Item import Item

import cv2
import numpy as np

class NumberFinder:
    @staticmethod
    def find_matches(number_field_image_gray, number, threshold=0.8) -> list:
        image = ImageProcessor.load_image(f'./numbers/{number}.png', grayscale=True)
        result = cv2.matchTemplate(number_field_image_gray, image, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)
        matches = []
        for pt in zip(*locations[::-1]):
            matches.append({
                'position': pt,
                'value': number,
            })
        return matches
    
    @staticmethod
    def extract_number(matches) -> int:
        if len(matches) == 0:
            return 1
        sorted_matches = sorted(matches, key=lambda num: num['position'])
        necessary_digits = NumberFinder.remove_unecessary(sorted_matches)
        return NumberFinder.mount_number(necessary_digits)

    @staticmethod
    def remove_unecessary(matches):
        current = matches[0]
        necessary_digits = []
        for i, match in enumerate(matches):
            if (not NumberFinder.is_equal_to(match, current)) or i == 0:
                necessary_digits.append(match)
        return necessary_digits

    @staticmethod
    def is_equal_to(this, other):
        tolerance = 5
        x, y = this['position']
        other_x, other_y = other['position']
        return (
            x < other_x + tolerance and x > other_x - tolerance
            and
            y < other_y + tolerance and y > other_y - tolerance
        )
    
    @staticmethod
    def mount_number(digits):
        number = ''
        for digit in digits:
            number += str(digit['value'])
        return int(number)