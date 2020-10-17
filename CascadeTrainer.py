import cv2 as cv2

 
################################################################

cameraNo = 0                      # CAMERA NUMBER
objectName = 'green'       # OBJECT NAME TO DISPLAY
frameWidth = 640                     # DISPLAY WIDTH
frameHeight = 480                  # DISPLAY HEIGHT
color= (255,255,255)
#################################################################
 
 
cap = cv2.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
 
def empty(a):
    pass
 
# CREATE TRACKBAR

cv2.namedWindow("Result")

cv2.resizeWindow("Result",frameWidth,frameHeight-300)

cv2.createTrackbar("Scale","Result",896,1000,empty)
cv2.createTrackbar("Neig","Result",1,50,empty)
cv2.createTrackbar("Min Area","Result",2500,100000,empty)
cv2.createTrackbar("Max Area","Result",11387,100000,empty)
cv2.createTrackbar("Brightness","Result",255,255,empty)

 
# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier("C:\\Users\\ayylmbo\\Desktop\\opencv\\sources\\data\\haarcascades\\haarcascade_green_led.xml")
cascade2 = cv2.CascadeClassifier("C:\\Users\\ayylmbo\\Desktop\\opencv\\sources\\data\\haarcascades\\haarcascade_blue_led.xml")
cascade3 = cv2.CascadeClassifier("C:\\Users\\ayylmbo\\Desktop\\opencv\\sources\\data\\haarcascades\\haarcascade_red_led.xml")
cascade4 = cv2.CascadeClassifier("C:\\Users\\ayylmbo\\Desktop\\opencv\\sources\\data\\haarcascades\\haarcascade_white_led.xml")

while True:
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # DETECT THE OBJECT USING THE CASCADE

    scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
    neig=cv2.getTrackbarPos("Neig", "Result")

    green = cascade.detectMultiScale(img,scaleVal,neig)
    blue = cascade2.detectMultiScale(img,scaleVal,neig)
    red = cascade3.detectMultiScale(img,scaleVal,neig)
    white = cascade4.detectMultiScale(img,scaleVal,neig)

    # DISPLAY THE DETECTED OBJECTS
    for (x,y,w,h) in green:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        maxArea = cv2.getTrackbarPos("Max Area", "Result")
        if area > maxArea:
            continue
        elif area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"Green",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
            roi_color = img[y:y+h, x:x+w]
        

    for (x,y,w,h) in blue:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        maxArea = cv2.getTrackbarPos("Max Area", "Result")
        if area > maxArea:
            continue
        elif area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Blue",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2)
            roi_color = img[y:y+h, x:x+w]

    for (x,y,w,h) in red:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        maxArea = cv2.getTrackbarPos("Max Area", "Result")
        if area > maxArea:
            continue
        elif area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Red",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2)
            roi_color = img[y:y+h, x:x+w]

    for (x,y,w,h) in white:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        maxArea = cv2.getTrackbarPos("Max Area", "Result")
        if area > maxArea:
            continue
        elif area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
            cv2.putText(img,"White",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)
            roi_color = img[y:y+h, x:x+w]
 
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break