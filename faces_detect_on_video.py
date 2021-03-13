# Ссылка на некоторые таблицы haar cascade:
# https://github.com/opencv/opencv/tree/master/data/haarcascades

# Импортируем библиотеку opencv
import cv2


def modify_frame(img, scale=1.0):
    # Изменяем размер исходного изображения
    # scale - Масштаб в долях процента
    img = cv2.resize(img, None, fx=scale, fy=scale)  # Изменение размера

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Преобразовываем в серый цвет

    haar_cascade = cv2.CascadeClassifier('haar_face.xml')  # Загружаем касадную таблицу
    faces_rect = haar_cascade.detectMultiScale(  # Функция библиотеки opencv для детекции объекта
        gray,  # Изображение
        scaleFactor=1.1,  # Коэффициент увеличения (min = 1.1)
        minNeighbors=10  # Коэффициент нахождения объекта минимального размера
    )  # Возвращает прямоугольники найденных объектов (номеров)

    print('Number of faces found = ', len(faces_rect))  # Выводим количество найденных лиц

    for (x, y, w, h) in faces_rect:  # Для каждого прямоугольника
        cv2.rectangle(img, (x, y), (x+w, y+h), (150, 255, 60), thickness=4)  # Рисуем прямоугольники

    return img  # Возвращает изображение с наложенными прямоугольниками найденных объектов


# Читаем видеопоток в бесконечном цикле
while True:
    is_closed = 0
    cap = cv2.VideoCapture('Media/Videos/film_1.mp4')

    while True:
        ret, frame = cap.read()  # Считываем кадр
        if ret:
            frame = modify_frame(frame, 0.5)  # Ищем контуры и накладываем их на кадр
            cv2.imshow('Video', frame)  # Выводим кадр на экран
            if cv2.waitKey(1) == 27:
                is_closed = 1  # По нажатию [Esc] в isclosed запишется 1
                break
        else:
            break

    if is_closed:
        break

cap.release()  # Освобождаем память от загруженного видео
cv2.destroyAllWindows()  # Уничтожаем все окна
