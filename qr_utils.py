import cv2
from pyzbar.pyzbar import decode

def scan_qr_from_image(img_path):
    img = cv2.imread(img_path)
    codes = decode(img)
    return [code.data.decode('utf-8') for code in codes]
