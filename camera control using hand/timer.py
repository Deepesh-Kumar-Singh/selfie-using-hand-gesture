import cv2
import time
timer=int(5)
video=cv2.VideoCapture(0)
i=int(1)
while True:
    res,frame=video.read()
    cv2.imshow("window",frame)
    k=cv2.waitKey(1)
    if(k==ord('t')):
        prevtime=time.time()
        timer=5
        while timer>=0:
            res,frame=video.read()
            cv2.rectangle(frame,(0,0),(250,50),(50,25,255),2,cv2.LINE_AA)
            cv2.putText(frame,'Timer:{}'.format(str(timer)),(20,30),cv2.FONT_HERSHEY_COMPLEX,1,color=(50,50,255),thickness=2)
            cv2.imshow('window',frame)
            cv2.waitKey(100)
            curr=time.time()
            if(curr-prevtime>1):
                prevtime=curr
                timer-=1
        else:
            res,frame=video.read()
            cv2.imshow("window",frame)
            cv2.waitKey(1000)
            cv2.imwrite('screenshot{}.jpg'.format(i),frame)
            i+=1

    if(k==ord('x')):
        break
video.release()
cv2.destroyAllWindows()