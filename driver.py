from detector import detect
from face_det import det
from video_capture import frame_cap
from QrCode_detect import decoder

def driver_func(Std_no):
    if decoder() == True:
        print("\n")
        Std_no +=1
        print("Capturing Student " + str(Std_no) + ".")
        print("\n")
        path = frame_cap(Std_no)
        print("Student " + str(Std_no) + " captured successfully.")
        print("\n")
        filename = path.split('/')
        print("Detecting face...")
        print("\n")
        detect(filename[1])
        print("Face detected Successfully!")
        det(filename[1])
    return Std_no

Std_no = 0

while True:
    print("\n")
    a = str(input('To register a student, press "Y" or press "q" to stop: '))
    if a == 'y'or a == 'Y':
        Std_no = driver_func(Std_no)
    else:
        break

print("Total students registered : {}".format(Std_no))
