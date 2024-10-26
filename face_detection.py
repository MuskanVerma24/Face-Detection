import cv2 as cv

live_capture = cv.VideoCapture(0)
opened = live_capture.isOpened()

if(opened):
    while(live_capture.isOpened()):
        success , frame = live_capture.read()

        if success == True:

            gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

            face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

            faces = face_cascade.detectMultiScale(gray_frame , 1.1 , 3)
 
            for (x,y,w,h) in faces:
                cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

            cv.imshow("Live Detection (Press esc to exit)",frame)

            if cv.waitKey(2)== 27:
                break

            

live_capture.release()
cv.destroyAllWindows()