# Сохранение видео испоьзуя OpenCV

# Импорт библиотек (модулей)
import cv2

# Открываем видео
video = cv2.VideoCapture('Media/Videos/film_1.mp4')

# Проверка что файл Не открыт и вывод ошибки
if not video.isOpened():
    print("Ошибка открытия файла")
else:
    # Узнаём исходное разрешение видео и конвертируем в целое число
    frame_width = int(video.get(3))  # Ширина
    frame_height = int(video.get(4))  # Высота

    # Размер изображения на основе разрешения (высоты и ширины кадра)
    size = (frame_width, frame_height)

    # Создаём переменную (объект) VideoWriter чтобы в дальнейшем
    # с её помощью сохранять кадры в файл 'result_filename.avi'.
    result = cv2.VideoWriter(
        'Media/Videos/result_filename.avi',  # Файл для сохраниения
        cv2.VideoWriter_fourcc(*'MJPG'),  # Кодек видео
        fps=10,  # frame per second
        frameSize=size  # Размер видео
    )

    while True:
        ret, frame = video.read()

        # Если кадр считался корректно, ret будет True
        if ret:
            # Делаем что-то с кадром

            result.write(frame)  # Запись кадра в 'filename.avi'

            cv2.imshow('Video', frame)  # Отображение кадра в окне 'Video'

            # Для остановки процесса можно нажать клавишу [s]
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break

        # Остановка цикла, если кадр не считался
        else:
            break

    # Когда всё выполнено освобождаем память объекта video и result
    video.release()
    result.release()

    # Закрываем все окна
    cv2.destroyAllWindows()

    print("Видео сохранено успешно")
