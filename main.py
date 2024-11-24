import cv2
import numpy as np
from utils import *
from data import items

inventory_image, gray_inventory_image = get_inventory_image('full1')
gray_item_image = get_item_image(items[2][0])

result = cv2.matchTemplate(gray_inventory_image, gray_item_image, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print(f"Valor máximo de correspondência: {max_val}")
print(f"Posição da correspondência: {max_loc}")

threshold = 0.5
if max_val >= threshold:
    print("O item está presente no inventário.")
else:
    print("O item NÃO está presente no inventário.")

w, h = gray_item_image.shape[::-1]
cv2.rectangle(inventory_image, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)

cv2.imshow('Resultado do Template Matching', inventory_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
