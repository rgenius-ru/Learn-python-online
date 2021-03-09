# Импортируем библиотеку opencv
import cv2

# Открывает
image_rgb = cv2.imread('Media/Photos/car.jpg')

# Изменяем размер исходного изображения
scale = 0.5  # В долях процента
image_rgb = cv2.resize(image_rgb, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)  # Изменение размера
# cv2.imshow('Image', image_color)  # Вывод исходного изображения


# image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)  # cvt - convert  # Преобразовываем в серый цвет
# cv2.imshow('Gray', image_gray) # Вывод серого изображения


# image_rgb = cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB) # преобразование BGR в RGB


# Загружаем касадную таблицу
cascade_table = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')


# Создаём функцию детекции гос номера автомобиля
def car_plate_detect(image):
    """
    :param image: изображение в любом цветовом пространстве
    :return: возвращает исходное изображение с наложенными прямоугольниками найденных номеров
    """
    img_copy = image.copy()  # Копируем исходное в новую переменую
    car_plate_rects = cascade_table.detectMultiScale(  # Функция библиотеки opencv детекции объекта
        img_copy,  # Копия изображения
        scaleFactor=1.1,  # Коэффициент увеличения (min = 1.1)
        minNeighbors=3  # Коэффициент нахождения объекта минимального размера
    )  # Возвращает прямоугольники найденных объектов (номеров)

    for x, y, w, h in car_plate_rects:  # Для каждого прямоугольника
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (255, 0, 0), 5)  # Рисуем прямоугольники

    return img_copy  # озвращает изображение с наложенными прямоугольниками найденных объектов


# Вызываем функция детекции гос номера автомобиля
result_img = car_plate_detect(image_rgb)  # image_rgb
cv2.imshow('Detect', result_img)  # Выводим изображение на экран

cv2.waitKey(0)  # Ожидаем нажатия клавиши до выхода
