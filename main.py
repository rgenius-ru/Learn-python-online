import cv2  # OpenCV


# Reading images
img1 = cv2.imread('Media/Photos/Snow-man1.jpeg')
img2 = cv2.imread('Media/Photos/Snow-man2.jpeg')
img3 = cv2.imread('Media/Photos/arms_6x6.png', cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread('Media/Photos/arms_64x64.png')


print(img1.shape)  # Вывод в косоль размер изображения и кол-во цветов


# Обрезка изображения (crop)
cv2.imshow('Image 1 croped', img1[:60, 500:560])


# Изменение яркости напрямую (не рекомендуется)
cv2.imshow('Image 3', img3)  # Исходное изображение
cv2.imshow('Image 3 + Brightness', img3 + 50)  # Изменнное изображение
print(img3 + 50)  # Вывод в консоль таблицы пикселей


# Изменение размеров изображения изображения
img4_scale = cv2.resize(img4, (200, 200))  # Функция изменения размера

cv2.imshow('Image 4', img4)  # Исходное изображение
cv2.imshow('Image 4 200x200', img4_scale)  # Изменнное изображение


# BGR исходное изображение
# cv2.imshow('Image 1', img1)

# Обычно в изображениях используется цветовое пространство RGB
# В openCV обычно используется - BGR

# BGR to GrayScale
# gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)
#
# # BGR to HSV
# hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HLS)
# cv2.imshow('HSV', hsv)
#
# # BGR to LAB
# lab = cv2.cvtColor(img1, cv2.COLOR_BGR2LAB)
# cv2.imshow('LAB', lab)
#
# b,g,r = cv2.split(img1)
#
# cv2.imshow('Blue', b)
# cv2.imshow('Green', g)
# cv2.imshow('Red', r)
#
# cv2.waitKey(0)


# Reading videos
# capture = cv2.VideoCapture('Media/Videos/1.mp4')
#
# while True:
#     isTrue, frame = capture.read()
#
#     if isTrue:
#         b, g, r = cv2.split(frame)
#         cv2.imshow('Video', frame)
#         cv2.imshow('Green', g)
#
#     if cv2.waitKey(20) & 0xFF==ord('d'):
#         break
#
# capture.release()
# cv2.destroyAllWindows()


cv2.waitKey(0)
