import cv2
# https://github.com/opencv/opencv/tree/master/data/haarcascades

img = cv2.imread('Media/Photos/task2/image4.jpg')


# Уменьшаем размер
scale = 1.0
img = cv2.resize(img, None, fx=scale, fy=scale)
# cv2.imshow('Source image', img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)


haar_cascade = cv2.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)


print('Number of faces found = ', len(faces_rect))


for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (150, 255, 60), thickness=4)

cv2.imshow('Detected faces', img)

cv2.waitKey()
