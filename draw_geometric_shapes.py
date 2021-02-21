import numpy as np
import cv2

img = np.zeros((400, 400, 3), dtype='uint8')  # Создаём изображение из 400х400х3 чёрных пикселей


# Usage: cv2.rectangle(image, angle1, angle2, color, thickness)
angle1 = (30, 30)  # (x, y)
angle2 = (300, 200)   # (x, y)
color = (0, 20, 200)  # (b, g, r)
thickness = 10
cv2.rectangle(img, angle1, angle2, color, thickness)  # Создаём квадрат


# Задание 1.
# Вывести в этом эе окне ещё один квадрат жёлтого цвета
# размером размером меньше красного.
# Enter your code HERE


cv2.imshow('Window', img)  # Выводим изображение на экран


cv2.waitKey(0)  # Ждём нажатия клавиши
cv2.destroyAllWindows()  # Уничтожаем все окна
