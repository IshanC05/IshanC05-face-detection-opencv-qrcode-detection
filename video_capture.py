import cv2
#from datetime import datetime

def frame_cap(n):
    #date_time = datetime.strftime("%Y_%m_%d-%I_%M_%S_%p")
    cap= cv2.VideoCapture(0)
    i=0
    while True:
        success, frame = cap.read()
        if success == False:
            break
        if i == 30:
            cv2.imwrite('Students/Student'+str(n)+'.jpg',frame)
            break
        i+=1
    filename = 'Students/Student'+str(n)+'.jpg'
    return filename