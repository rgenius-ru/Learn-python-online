import cv2
import numpy as np


def on_change(val):
    # Создаём маску
    min_color = np.array([0, 0, 0])  # Минимальные значения [r_min, g_min, b_min]
    max_color = np.array([255, 255, val])  # Максимальные значения [r_max, g_max, b_max]

    mask = cv2.inRange(img, min_color, max_color)
    cv2.imshow('Image', mask)


img = cv2.imread('Media/Photos/task2/image1.jpg')

cv2.imshow('Image', img)

cv2.createTrackbar('Slider', 'Image', 127, 255, on_change)

cv2.waitKey(0)
cv2.destroyAllWindows()
