import cv2

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
