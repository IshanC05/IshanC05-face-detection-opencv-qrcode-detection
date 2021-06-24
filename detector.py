import cv2

def detect(filename):
    face_cascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    img = cv2.imread('Students/'+filename)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(imgGray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30))

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w+10, y+h+10), (0,255,0), 2)
        roi_color = img[y:y+h+10, x:x+w+10]
        cv2.imwrite('detected_faces/' + str(filename) + '_face.jpg', roi_color)