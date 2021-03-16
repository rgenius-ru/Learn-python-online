# Изучение метода cv2.imwrite()

# Импортируем библиотеки (модули)
import cv2
import os

# Открываем изображение
img = cv2.imread('Media/Photos/lighting-happy2.jpg')

# Делаем что-то с изображением


# Сохраняем изображение
cv2.imwrite('Media/Photos/result-image.jpg', img)

print('Изображение сохранено успешно')
