import cv2


img = cv2.imread('Media/Photos/lighting-happy2.jpg')


# Уменьшаем размер
scale = 0.5
img = cv2.resize(img, None, fx=scale, fy=scale)
# cv2.imshow('Source image', img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)


haar_cascade = cv2.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)


print('Number of faces found = ', len(faces_rect))


for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv2.imshow('Detected faces', img)

cv2.waitKey()
