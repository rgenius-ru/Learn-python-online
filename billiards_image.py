import cv2  # OpenCV
import numpy as np

sourse_img = cv2.imread('Media/Photos/billiards/billiards.png')

# Уменьшаем размер
scale = 0.75
resized_img = cv2.resize(sourse_img, None, fx=scale, fy=scale)


# Вывод изображения на экран
cv2.imshow('Original Resized Image', resized_img)


# Конвертируем в цветовое пространство HSV
# BGR to HSV (Hue Saturation Value - Оттенок Насыщенность Значение\Яркость)
hsv = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)


# Создаём маску
min_color = np.array([0, 0, 200])  # Минимальные значения
max_color = np.array([100, 100, 255])  # Максимальные значения

mask = cv2.inRange(hsv, min_color, max_color)
cv2.imshow('Mask', mask)


# Создаём контуры
ret, threshold = cv2.threshold(mask, 250, 255, 0)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

count_contours = len(contours)

print(f'Всего найдено {count_contours} контуров.')

img_with_all_contours = resized_img
cv2.drawContours(img_with_all_contours, contours, -1, (0, 0, 255), 2)
cv2.imshow('Resized image with all contours', img_with_all_contours)


# Определяем минимальную площадь контура
list_areas = []
for contour in contours:
    area = cv2.contourArea(contour)
    list_areas.append(area)

list_areas.sort()
print(list_areas)


# Создаём список только больших контуров
threshold_area = 150
list_big_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > threshold_area:
        list_big_contours.append(contour)

print(f'Найдено {len(list_big_contours)} контуров, площадью больше {threshold_area}')


# Выводим контуры на изображении
img_with_big_contours = resized_img
cv2.drawContours(img_with_big_contours, list_big_contours, -1, (255, 0, 0), 2)
cv2.imshow('Resized image with only big contours', img_with_big_contours)


# Ждём нажатия клавиши
cv2.waitKey(0)
