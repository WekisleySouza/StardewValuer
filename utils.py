import cv2
import numpy as np

def get_inventory_image(name):
    img = cv2.imread(f'./inventory/{name}.png')
    if img is None:
        print("Erro ao carregar o inventário!")
        exit()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img, img_gray

def get_item_image(name):
    img = cv2.imread(f'./items/{name}.png', cv2.IMREAD_UNCHANGED)
    
    if img is None:
        print("Erro ao carregar o item!")
        exit()
    if img.shape[2] == 4:
        img = process_alpha_channel(img, (108, 178, 239))

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray

def process_alpha_channel(image, bg_color=(255, 255, 255)):
    bgr = image[:, :, :3]
    alpha = image[:, :, 3]
    
    background = np.full(bgr.shape, bg_color, dtype=np.uint8)
    
    alpha_mask = alpha[:, :, np.newaxis] / 255.0
    result = cv2.convertScaleAbs(bgr * alpha_mask + background * (1 - alpha_mask))
    return result
    
def testar():
    img = get_item_image('morel')
    print(img.shape)
    cv2.imshow('Resultado do Template Matching', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    testar()