# Ссылка на некоторые таблицы haar cascade:
# https://github.com/opencv/opencv/tree/master/data/haarcascades

# Импортируем библиотеку opencv
import cv2

img = cv2.imread('Media/Photos/task2/image4.jpg')  # Открываем изображение
img_copy = img.copy()  # Копируем исходное изображение в новую переменую

# Изменяем размер исходного изображения
scale = 1.0  # Масштаб в долях процента
img_copy = cv2.resize(img_copy, None, fx=scale, fy=scale)  # Изменение размера
# cv2.imshow('Source image', img)  # Вывод исходного изображения

gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)  # Преобразовываем в серый цвет
# cv2.imshow('Gray', gray)  # Вывод серого изображения

haar_cascade = cv2.CascadeClassifier('haar_face.xml')  # Загружаем касадную таблицу
faces_rect = haar_cascade.detectMultiScale(  # Функция библиотеки opencv для детекции объекта
    gray,  # Изображение
    scaleFactor=1.1,  # Коэффициент увеличения (min = 1.1)
    minNeighbors=3  # Коэффициент нахождения объекта минимального размера
)  # Возвращает прямоугольники найденных объектов (номеров)

print('Number of faces found = ', len(faces_rect))  # Выводим количество найденных лиц

for (x, y, w, h) in faces_rect:  # Для каждого прямоугольника
    cv2.rectangle(img_copy, (x, y), (x+w, y+h), (150, 255, 60), thickness=4)  # Рисуем прямоугольники

cv2.imshow('Detected faces', img_copy)  # Выводим изображение на экран

cv2.waitKey()  # Ожидаем нажатия клавиши до выхода
