import cv2  # OpenCV
import numpy as np


def modify_frame(sourse_img):
    # Конвертируем в цветовое пространство HSV
    # BGR to HSV (Hue Saturation Value - Оттенок Насыщенность Значение\Яркость)
    hsv = cv2.cvtColor(sourse_img, cv2.COLOR_BGR2HSV)
    #cv2.imshow('HSV', hsv)

    # Создаём маску
    min_color = np.array([0, 0, 200])  # Минимальные значения
    max_color = np.array([100, 100, 255])  # Максимальные значения

    mask = cv2.inRange(hsv, min_color, max_color)
    cv2.imshow('Mask', mask)

    # Создаём контуры
    ret, threshold = cv2.threshold(mask, 250, 255, 0)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Создаём список только больших контуров
    threshold_area = 150
    list_big_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > threshold_area:
            list_big_contours.append(contour)

    # Накладываем контуры на изображение
    img_with_big_contours = sourse_img
    cv2.drawContours(img_with_big_contours, list_big_contours, -1, (255, 0, 0), 2)

    return img_with_big_contours


# Reading videos
while True:
    isclosed = 0
    cap = cv2.VideoCapture('Media/Videos/billiards_video1.mp4')

    while True:
        ret, frame = cap.read()  # Считываем кадр
        if ret:
            frame = modify_frame(frame)  # Ищем контуры и накладываем их на кадр
            cv2.imshow('Video', frame)  # Выводим кадр на экран
            if cv2.waitKey(1) == 27:
                isclosed = 1  # When esc is pressed isclosed is 1
                break
        else:
            break

    if isclosed:
        break


cap.release()  # Освобождаем память от загруженного видео
cv2.destroyAllWindows()  # Уничтожаем все окна
