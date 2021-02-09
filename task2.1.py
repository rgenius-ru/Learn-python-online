import cv2  # OpenCV

img1 = cv2.imread('Media/Photos/task2/image4.jpg')

# Обычно в изображениях используется цветовое пространство RGB
# В openCV обычно используется - BGR

img1 = cv2.resize(img1, (1124//2, 845//2))

# BGR исходное изображение
cv2.imshow('Image 1', img1)


# Разделение BGR на отдельные каналы цвета
b, g, r = cv2.split(img1)

cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)


# # BGR to GrayScale
# gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)


# # BGR to HSV (Hue Saturation Value - Оттенок Насыщенность Значение\Яркость)
# hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HLS)
# cv2.imshow('HSV', hsv)
#
# # Разделение HSV на отдельные каналы цвета
# h, s, v = cv2.split(hsv)
#
# cv2.imshow('HSV h channel', h)
# cv2.imshow('HSV s channel', s)
# cv2.imshow('HSV v channel', v)


# # BGR to LAB
# lab = cv2.cvtColor(img1, cv2.COLOR_BGR2LAB)
# cv2.imshow('LAB', lab)
#
# # Разделение LAB на отдельные каналы цвета
# lab_l, lab_a, lab_b = cv2.split(lab)
#
# cv2.imshow('Lab L channel', lab_l)
# cv2.imshow('Lab A channel', lab_a)
# cv2.imshow('Lab B channel', lab_b)


# Ждём нажатия клавиши
cv2.waitKey(0)
