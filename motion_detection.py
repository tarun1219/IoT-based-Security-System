import cv2
ff=None
video=cv2.VideoCapture(0)
while True:
    check, f = video.read()
    status=0
    demo=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    demo=cv2.GaussianBlur(demo,(21,21),0)
    if ff is None:
        ff=demo
        continue
    a=cv2.absdiff(ff,demo)                                       
    b=cv2.threshold(a, 30, 255, cv2.THRESH_BINARY)[1]
    b=cv2.dilate(b, None, iterations=2)
    (cnts,_)=cv2.findContours(b.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in cnts:
        if cv2.contourArea(i) < 10000 :
            continue
        (x, y, w, h)=cv2.boundingRect(i)                                        
        cv2.rectangle(f, (x, y), (x+w, y+h), (100,100,100), 3)

    cv2.imshow("Color Frame",f)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows

