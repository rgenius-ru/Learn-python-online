# TODO something
# Задание 1.
# Вывести на экран исходное изображение файла: "Media/Photos/task2/dcode.png"
# Вывести на экран три изображения: канал красного, зелёного и синего.

import cv2  # OpenCV

img1 = cv2.imread('Media/Photos/task2/dcode.png')

# BGR исходное изображение
cv2.imshow('Image 1', img1)


# Разделение BGR на отдельные каналы цвета
b, g, r = cv2.split(img1)

cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)


# Ждём нажатия клавиши
cv2.waitKey(0)
