import cv2

image_color = cv2.imread('Media/Photos/car.jpg')

scale = 0.5
image_color = cv2.resize(image_color, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Image', image_color)

image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)  # cvt - convert
cv2.imshow('Gray', image_gray)

image_rgb = cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB)

# Import Haar Cascade XML file for Russian car plate numbers
carplate_haar_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')


# Setup function to detect car plate
def carplate_detect(image):
    carplate_overlay = image.copy()
    carplate_rects = carplate_haar_cascade.detectMultiScale(carplate_overlay, scaleFactor=1.1, minNeighbors=3)
    for x, y, w, h in carplate_rects:
        cv2.rectangle(carplate_overlay, (x, y), (x + w, y + h), (255, 0, 0), 5)

    return carplate_overlay


detected_carplate_img = carplate_detect(image_rgb)
cv2.imshow('Detect', detected_carplate_img)

cv2.waitKey(0)
