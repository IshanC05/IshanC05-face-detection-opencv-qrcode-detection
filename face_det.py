import cv2

def det(filename):
    faceCascade= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    img = cv2.imread('Students/'+filename)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w+10, y+h+10), (0,255,0), 2)
        cv2.imwrite('detection/' + str(filename) + '_face.jpg', img)
        #cv2.imshow("Result" ,img)
        #cv2.waitKey(0)