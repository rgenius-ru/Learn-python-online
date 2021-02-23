import cv2  # OpenCV
import numpy as np

sourse_img = cv2.imread('Media/Photos/billiards/danger-weapon.jpg')  # Исходное изображение

# Уменьшаем размер
scale = 1.0
resized_img = cv2.resize(sourse_img, None, fx=scale, fy=scale)


# Вывод изображения на экран
cv2.imshow('Original Resized Image', resized_img)


# Конвертируем в цветовое пространство HSV
# BGR to HSV (Hue Saturation Value - Оттенок Насыщенность Значение\Яркость)
hsv = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)


# Создаём маску
min_color = np.array([100, 100, 110])  # Минимальные значения [r_min, g_min, b_min]
max_color = np.array([120, 200, 255])  # Максимальные значения [r_max, g_max, b_max]

mask = cv2.inRange(hsv, min_color, max_color)
cv2.imshow('Mask', mask)


# Создаём контуры
ret, threshold = cv2.threshold(mask, 250, 255, 0)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# count_contours = len(contours)
#
# print(f'Всего найдено {count_contours} контуров.')
#
# img_with_all_contours = resized_img
# cv2.drawContours(img_with_all_contours, contours, -1, (255, 0, 0), 2)
# cv2.imshow('Resized image with all contours', img_with_all_contours)


# Находим площадь каждого контура и определяем минимальную площадь
list_areas = []
for contour in contours:
    area = cv2.contourArea(contour)
    list_areas.append(area)

list_areas.sort()
print(list_areas)


# Создаём список только больших контуров
threshold_area_min = 1000
threshold_area_max = 100000

list_big_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if threshold_area_min < area < threshold_area_max:
        list_big_contours.append(contour)

print(f'Найдено {len(list_big_contours)} контуров, площадью больше {threshold_area_min} и меньше {threshold_area_max}')


# Выводим контуры на изображении
img_with_big_contours = resized_img
cv2.drawContours(img_with_big_contours, list_big_contours, -1, (0, 0, 255), 2)
cv2.imshow('Resized image with only big contours', img_with_big_contours)


# Ждём нажатия клавиши
cv2.waitKey(0)
