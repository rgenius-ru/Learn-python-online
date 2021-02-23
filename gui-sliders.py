import cv2
import numpy as np


hue_min = 0
hue_max = 255

saturation_min = 0
saturation_max = 255

value_min = 0
value_max = 255


def on_change_hue_min(val):
    global hue_min
    hue_min = val
    update_mask_image()


def on_change_hue_max(val):
    global hue_max
    hue_max = val
    update_mask_image()


def on_change_saturation_min(val):
    global saturation_min
    saturation_min = val
    update_mask_image()


def on_change_saturation_max(val):
    global saturation_max
    saturation_max = val
    update_mask_image()


def on_change_value_min(val):
    global value_min
    value_min = val
    update_mask_image()


def on_change_value_max(val):
    global value_max
    value_max = val
    update_mask_image()


def update_mask_image():
    # Создаём маску
    min_color = np.array([hue_min, saturation_min, value_min])  # Минимальные значения [r_min, g_min, b_min]
    max_color = np.array([hue_max, saturation_max, value_max])  # Максимальные значения [r_max, g_max, b_max]

    mask = cv2.inRange(hsv, min_color, max_color)
    cv2.imshow('Mask', mask)


img = cv2.imread('Media/Photos/billiards/white-cat.jpg')


# Конвертируем в цветовое пространство HSV
# BGR to HSV (Hue Saturation Value - Оттенок Насыщенность Значение\Яркость)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)


window_name = 'Mask'
update_mask_image()


cv2.createTrackbar('h min', window_name, 0, 255, on_change_hue_min)
cv2.createTrackbar('h max', window_name, 255, 255, on_change_hue_max)

cv2.createTrackbar('s min', window_name, 0, 255, on_change_saturation_min)
cv2.createTrackbar('s max', window_name, 255, 255, on_change_saturation_max)

cv2.createTrackbar('v min', window_name, 0, 255, on_change_value_min)
cv2.createTrackbar('v max', window_name, 255, 255, on_change_value_max)


cv2.waitKey(0)
cv2.destroyAllWindows()
