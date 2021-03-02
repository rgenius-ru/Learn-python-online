import cv2
import numpy as np


min = 0
max = 255


def on_change_min(val):
    global min
    min = val
    # Создаём маску
    min_color = np.array([0, 0, min])  # Минимальные значения [r_min, g_min, b_min]
    max_color = np.array([255, 255, max])  # Максимальные значения [r_max, g_max, b_max]

    mask = cv2.inRange(img, min_color, max_color)
    cv2.imshow('Image', mask)
    print(min, max)


def on_change_max(val):
    global max
    max = val
    # Создаём маску
    min_color = np.array([0, 0, min])  # Минимальные значения [r_min, g_min, b_min]
    max_color = np.array([255, 255, max])  # Максимальные значения [r_max, g_max, b_max]

    mask = cv2.inRange(img, min_color, max_color)
    cv2.imshow('Image', mask)
    print(min, max)



img = cv2.imread('Media/Photos/task2/image1.jpg')

cv2.imshow('Image', img)

cv2.createTrackbar('Slider min', 'Image', 127, 255, on_change_min)
cv2.createTrackbar('Slider max', 'Image', 127, 255, on_change_max)

cv2.waitKey(0)
cv2.destroyAllWindows()
