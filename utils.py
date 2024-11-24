import cv2
import numpy as np

def get_inventory_image(name):
    img = cv2.imread(f'./inventories/{name}.png')
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

def print_result_on_image(image, text):
    width = image.shape[1]
    text_size = cv2.getTextSize(str(text), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
    text_x = width - text_size[0] - 10
    text_y = 30
    cv2.putText(image, str(text), (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
def match_with_orb(image1, image2):
    # Inicializa o detector ORB
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(image1, None)
    kp2, des2 = orb.detectAndCompute(image2, None)

    # Verifica se os descritores foram gerados
    if des1 is None or des2 is None:
        print("Nenhum descritor encontrado em uma das imagens.")
        return [], kp1, kp2  # Retorna correspondências vazias

    # Matcher de descritores (Hamming distance)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    # Ordena as correspondências pelo menor erro (distância)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches, kp1, kp2


def testar():
    img = get_item_image('morel')
    print(img.shape)
    cv2.imshow('Resultado do Template Matching', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    testar()