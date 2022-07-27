import cv2 as cv 
import numpy as np
import time
# Distance constants 
KNOWN_DISTANCE = 45 #cm
ROBOTCAR_WIDTH = 20 #INCHES
BIKE_WIDTH = 3.0 #INCHES
MOTOR_WIDTH = 3.0

# Object detector constant 
CONFIDENCE_THRESHOLD = 0.3
NMS_THRESHOLD = 0.3

# colors for object detected
COLORS = [(255,0,0),(255,0,255),(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
GREEN =(0,255,0)
BLACK =(0,0,0)
# defining fonts 
FONTS = cv.FONT_HERSHEY_COMPLEX

# getting class names from classes.txt file 
class_names = []
with open("classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
#  setttng up opencv net
yoloNet = cv.dnn.readNet('yolov4-tiny-custom_last (3).weights', 'yolov4-tiny-custom.cfg')

#yoloNet.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
#yoloNet.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)

model = cv.dnn_DetectionModel(yoloNet)
model.setInputParams(size=(96, 96), scale=1/255, swapRB=True)

# object detector funciton /method
def object_detector(image):
    classes, scores, boxes = model.detect(image, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    # creating empty list to add objects data
    data_list =[]
    for (classid, score, box) in zip(classes, scores, boxes):
        # define color of each, object based on its class id 
        color= COLORS[int(classid) % len(COLORS)]
    
        label = "%s : %f" % (class_names[classid[0]], score)

        # draw rectangle on and label on object
        cv.rectangle(image, box, color, 2)
        cv.putText(image, label, (box[0], box[1]-14), FONTS, 0.5, color, 2)
    
        # getting the data 
        # 1: class name  2: object width in pixels, 3: position where have to draw text(distance)
        if classid == 0:  # class id
            data_list.append([class_names[classid[0]], box[2], (box[0], box[1] - 2)])
        '''elif classid == 1:
            data_list.append([class_names[classid[0]], box[2], (box[0], box[1] - 2)])
        elif classid == 2:
            data_list.append([class_names[classid[0]], box[2], (box[0], box[1] - 2)])'''
        # if you want inclulde more classes then you have to simply add more [elif] statements here
        # returning list containing the object data. 
    return data_list

def focal_length_finder (measured_distance, real_width, width_in_rf):
    focal_length = (width_in_rf * measured_distance) / real_width

    return focal_length

# distance finder function 
def distance_finder(focal_length, real_object_width, width_in_frmae):
    distance = (real_object_width * focal_length) / width_in_frmae
    return distance

# reading the reference image from dir 

ref_robotcar = cv.imread('test.jpg')
ROBOTCAR_data = object_detector(ref_robotcar)
ROBOTCAR_width_in_rf = ROBOTCAR_data[0][1]
#ROBOTCAR_width_in_rf = 410

BIKE_width_in_rf = 250

MOTOR_width_in_rf = 250

print(f" ROBOTCAR width in pixels : {ROBOTCAR_width_in_rf} BIKE width in pixel: {BIKE_width_in_rf} MOTOR width in pixel: {MOTOR_width_in_rf}")

# finding focal length 
focal_ROBOTCAR = focal_length_finder(KNOWN_DISTANCE, ROBOTCAR_WIDTH, ROBOTCAR_width_in_rf)
focal_BIKE = focal_length_finder(KNOWN_DISTANCE, BIKE_WIDTH, BIKE_width_in_rf)
focal_MOTOR = focal_length_finder(KNOWN_DISTANCE, MOTOR_WIDTH, MOTOR_width_in_rf)
cap = cv.VideoCapture(1)
prev_frame_time = 0
new_frame_time = 0
temp = 0
xuat_data = open("data.txt","w+")
while True:
    ret, frame = cap.read()
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time

    cv.putText(frame, "fps =  ", (20, 50), FONTS, 0.7, (0, 0, 255), 2)
    cv.putText(frame, str(int(fps)), (95, 50), FONTS, 0.7, (0, 0, 255), 2)
    data = object_detector(frame)
    for d in data:
        if d[0] == 'robotcar':
            distance = distance_finder(focal_ROBOTCAR, ROBOTCAR_WIDTH, d[1])
            x, y = d[2]
        '''elif d[0] == 'bike':
            distance = distance_finder(focal_BIKE, BIKE_WIDTH, d[1])
            x, y = d[2]
        elif d[0] == 'motor':
            distance = distance_finder(focal_MOTOR, MOTOR_WIDTH, d[1])
            x, y = d[2]'''
        v= (distance - temp)*fps/10

        temp = distance

        cv.rectangle(frame, (x, y - 3), (x + 150, y + 23), BLACK, -1)
        cv.putText(frame, f'vantoc: {round(v, 2)} m/s', (x + 5, y + 50), FONTS, 0.48, BLACK, 2)
        cv.putText(frame, f'Dis: {round(distance, 2)} cm', (x + 5, y + 13), FONTS, 0.48, GREEN, 2)
        '''now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")'''
        data = (str(v))  + "\n"
        print(data)
        xuat_data.write(data)
        #print(data)


    cv.imshow('frame',frame)
    
    key = cv.waitKey(1)
    if key ==ord('q'):
        xuat_data.close()
        break
cv.destroyAllWindows()
cap.release()

