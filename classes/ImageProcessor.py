import cv2
import numpy as np

class ImageProcessor:
    @staticmethod
    def load_image(path, grayscale=False):
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED if not grayscale else cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError(f"Erro ao carregar a imagem: {path}")
        return img

    @staticmethod
    def draw_text(image, text, position, color=(255, 255, 255), size=0.8, thickness=2):
        cv2.putText(image, str(text), position, cv2.FONT_HERSHEY_SIMPLEX, size, color, thickness)

    @staticmethod
    def draw_rectangle(image, top_left, bottom_right, color=(0, 0, 255), thickness=2):
        cv2.rectangle(image, top_left, bottom_right, color, thickness)

    @staticmethod
    def crop_image(image, top_left, bottom_right):
        x1, y1 = top_left
        x2, y2 = bottom_right
        return image[y1:y2, x1:x2]
    
    @staticmethod
    def detect_dominant_color(image, colors):
        # Converte a imagem para HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        color_counts = {color_name: 0 for color_name in colors.keys()}
        total_pixels = image.shape[0] * image.shape[1]
        
        for color_name, (lower, upper) in colors.items():
            mask = cv2.inRange(hsv_image, np.array(lower), np.array(upper))
            color_counts[color_name] = np.count_nonzero(mask)
        
        dominant_color = max(color_counts, key=color_counts.get)
        
        if color_counts[dominant_color] / total_pixels > 0.5:
            return dominant_color
        return "unknown"

