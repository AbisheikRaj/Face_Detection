#deduct a single image 
'''import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Deduct front-face position

image = cv2.imread('D:\SmileDeduction\AkshayKumar.jpg') #import image with open cv2
#image = cv2.imread('D:\SmileDeduction\group2.jpg')
#Note visit Opencv Documentation
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Convert the image to grayscale
#cv2.cvtColor() --- convert the image colour
#cv2.COLOR_BGR2GRAY --- convert background to grayscale


# detect face (it retuns the face coordinates)
face_coordinates = trained_face_data.detectMultiScale(grayscale_image)
#print(face_coordinates)   [[209  88 230 230]] = [[x y width height]] list of list
for (x, y, w, h) in face_coordinates:
    #cv2.rectangle(image, (209, 88), (209 + 230, 88 + 230), (0, 255, 0), 2)
    #cv2.rectangle(image, (x, y), (x + w), (y + h), RGB color coordinates, width of the line)
    cv2.rectangle(image, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 5)




cv2.imshow("Face Deductor", image) # It is used for show the image
cv2.waitKey() # pause the execution of the code for showing the image





print("code completed")
'''

#Detect image in web-camera or video clips
import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Deduct front-face position

webcam = cv2.VideoCapture(0) # videocapture 0 ----> webcamera , use the directoy of the video
while True:
    successful_frame_read, frame = webcam.read() #it returns boolean and frames

    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscale_image)
    
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 5)
    
    cv2.imshow("Face Deductor", frame) # It is used for show the image
    key = cv2.waitKey(1) # 0 --> delay(ms) pause the execution of the code for showing the image
    if (key == 81 or key == 113): #ascii value of the character for Q and q
        break
    
webcam.release()

print("Finished")