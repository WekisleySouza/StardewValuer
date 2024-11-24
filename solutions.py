import cv2
import numpy as np
from utils import *
from data import items

def print_item_info(name, max_val, max_loc):
        print(20*"-=")
        print(f"Item: {name}")
        print(20*"-=")
        print(f"Valor máximo de correspondência de: {max_val}")
        print(f"Posição da correspondência de: {max_loc}")

def run_match_template():
    inventory_image, gray_inventory_image = get_inventory_image('in8')
    found_items = []

    for item in items:

        gray_item_image = get_item_image(item['name'])

        result = cv2.matchTemplate(gray_inventory_image, gray_item_image, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # print_item_info(item['name'], max_val, max_loc)

        threshold = 0.7
        if max_val >= threshold:
            w, h = gray_item_image.shape[::-1]
            price_index = 1

            found_items.append({
                'name': item['name'],
                'price': item[f'price{price_index}'],
                'width': w,
                'heigth': h,
                'min_loc': min_loc,
                'max_loc': max_loc
            })

    sum = 0
    for item in found_items:
        cv2.rectangle(inventory_image, item['max_loc'], (item['max_loc'][0] + item['width'], item['max_loc'][1] + item['heigth']), (0, 0, 255), 2)
        sum += item['price']

    print_result_on_image(inventory_image, f'${sum}')

    cv2.imshow('Resultado do Template Matching', inventory_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()