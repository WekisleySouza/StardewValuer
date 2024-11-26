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
    inventory_image, gray_inventory_image = get_inventory_image('in3')
    found_items = []

    for item in items:
        gray_item_image = get_item_image(item['name'])

        # Executa template matching
        result = cv2.matchTemplate(gray_inventory_image, gray_item_image, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8  # Limiar de correspondência
        w, h = gray_item_image.shape[::-1]

        # Encontra todas as localizações com correspondência acima do limiar
        locations = np.where(result >= threshold)
        n_loc = 0

        # Inverte e organiza as coordenadas
        for pt in zip(*locations[::-1]): 
            if not is_in_list(pt, found_items):
                n_loc += 1
                found_items.append({
                    'name': item['name'],
                    'price': item[f'price1'],
                    'top_left': pt,
                    'bottom_right': (pt[0] + w + 5, pt[1] + h + 25),
                    'width': w,
                    'height': h
                })

        print(f"Encontradas {n_loc} correspondências para {item['name']}")

    # Soma os preços e marca itens
    total_sum = 0
    for item in found_items:
        total_sum += item['price']
        cv2.rectangle(inventory_image, item['top_left'], item['bottom_right'], (0, 0, 255), 2)

    # Adiciona o total à imagem
    print_result_on_image(inventory_image, f'${total_sum}')

    # Mostra o resultado
    cv2.imshow('Resultado do Template Matching', inventory_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
