import cv2


# Reading images
img1 = cv2.imread('Media/Photos/Snow-man1.jpeg')
img2 = cv2.imread('Media/Photos/Snow-man2.jpeg')
img3 = cv2.imread('Media/Photos/arms_6x6.png', cv2.IMREAD_GRAYSCALE)

#print(img3[:3])
print(img3)
#print(img1)

#cv2.imshow('Image 1', img1[:200])
#cv2.imshow('Image 2', img2)
cv2.imshow('Image 3', img3[:3])

cv2.waitKey(0)

#print(img3)

# cv2.imshow('Image1', img1)
# cv2.imshow('Image2', img2[:100])

#Reading videos
# capture = cv2.VideoCapture('Media/Videos/1.mp4')
#
# while True:
#     isTrue, frame = capture.read()
#     cv2.imshow('Video', frame)
#
#     if cv2.waitKey(20) & 0xFF==ord('d'):
#         break
#
# capture.release()
# cv2.destroyAllWindows()

#cv2.waitKey(0)