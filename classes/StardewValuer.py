from classes.ImageProcessor import ImageProcessor
from classes.ItemFinder import ItemFinder
from classes.Item import Item

import cv2

class StardewValuer:
    def __init__(self, inventory_image_path):
        self.inventory_image = ImageProcessor.load_image(inventory_image_path)
        self.inventory_gray = cv2.cvtColor(self.inventory_image, cv2.COLOR_BGR2GRAY)
        self.detected_items = []

    def find_items(self, items):
        for item in items:
            matches = ItemFinder.find_matches(self.inventory_gray, item)
            
            for match in matches:
                if not self.is_duplicate(match):
                    self.detected_items.append(match)

    def is_duplicate(self, match: Item):
        for item in self.detected_items:
            if match.is_equal_to(item):
                return True
        return False
    
    def find_stars(self, colors):
        for item in self.detected_items:
            item_image = ImageProcessor.crop_image(self.inventory_image, item.star_top_left_position, item.star_bottom_right_position)
            item.star = ImageProcessor.detect_dominant_color(item_image, colors)
    
    def find_numbers(self, numbers):
        ...

    def calculate_total_value(self):
        return sum(item.price for item in self.detected_items)
    
    def display_results(self):
        for item in self.detected_items:
            ImageProcessor.draw_rectangle(
                self.inventory_image, item.position, item.bottom_right_position, item.star_color
            )
            ImageProcessor.draw_rectangle(
                self.inventory_image, item.star_top_left_position, item.star_bottom_right_position,
                color=(255, 255, 0)
            )
            # ImageProcessor.draw_rectangle(
            #     self.inventory_image, item.number_top_left_position, item.number_bottom_right_position,
            #     color=(0, 255, 0)
            # )
        ImageProcessor.draw_text(self.inventory_image, f'${self.calculate_total_value()}', (10, 30))
        cv2.imshow('Inventory Analysis', self.inventory_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()