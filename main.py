import cv2  # OpenCV


# Reading images
img1 = cv2.imread('Media/Photos/Snow-man1.jpeg')
img2 = cv2.imread('Media/Photos/Snow-man2.jpeg')
img3 = cv2.imread('Media/Photos/arms_6x6.png', cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread('Media/Photos/arms_64x64.png')

img4_scale = cv2.resize(img4, (200, 200))

#print(img1.shape)


print(img3 + 50)
# print(type(img3))

#cv2.imshow('Image 1', img1[:6, 500:506])

cv2.imshow('Image 3', img3)
cv2.imshow('Image 3 + Brightness', img3 + 50)

cv2.imshow('Image 4', img4)
cv2.imshow('Image 4 200x200', img4_scale)

# BGR исходное изображение
cv2.imshow('Image 1', img1)

# Обычно используется в изображениях RGB
# В openCV обычно используется BGR

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


#Reading videos
capture = cv2.VideoCapture('Media/Videos/1.mp4')


while True:
    isTrue, frame = capture.read()


    if isTrue:
        b, g, r = cv2.split(frame)
        cv2.imshow('Video', frame)
        cv2.imshow('Green', g)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()

cv2.waitKey(0)