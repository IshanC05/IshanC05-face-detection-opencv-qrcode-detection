import os
import cv2
from datetime import date

def decoder():
    def file_exists_or_not(file_path):
        return os.path.isfile(file_path)

    def string_to_be_searched(file_name, string_to_search):
        x = file_exists_or_not(file_name)
        if x:
            with open(file_name, 'r' ) as read_obj:
                for line in read_obj:
                    if string_to_search == line:
                        date_obj = line.split(',')
                        print("Attendace for the person for", date_obj[0], "is already marked.")
                        return None
            return 1
        else:
            return 0

    file_path = 'C:/Users/Ishan/Desktop/BE Project code/info.txt'   #To be changed

    d = date.today().strftime("%d-%m-%Y")
    cap = cv2.VideoCapture(0)

    detector = cv2.QRCodeDetector()
    print("Searching for QR Code...")

    while True:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)

        if data:
            #print("data found: ", data)
            data_temp = data.split()
            data = ','.join(data_temp)
            whole_info = str(d) + ',' + data + "\n"
            out = string_to_be_searched(file_path, whole_info)
            
            #File does not exist. Creating one...
            if out != None:
                if out == 0:
                    print("Marking attendance.")
                    with open(file_path, 'a') as f:
                        f.write(whole_info)
                    print("Attendance successfully marked!")

                #File exists. Appending to it...
                elif out == 1:
                    print("Marking attendance.")
                    with open(file_path, 'a') as f:
                        f.write(whole_info)
                    print("Attendance successfully marked!")
                return True
            else:
                return False
    cap.release()