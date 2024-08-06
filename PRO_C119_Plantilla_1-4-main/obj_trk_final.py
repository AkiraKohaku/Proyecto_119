import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

video = cv2.VideoCapture("footvolleyball.mp4")
# Carga el rastreador
tracker = cv2.TrackerCSRT_create()

# Lee el primer cuadro del video
success,img = video.read()

# Selecciona el campo delimitador en la imagen
bbox = cv2.selectROI("rastreando",img,False)

# Inicializa el rastreador en la imagen y el campo delimitador
tracker.init(img,bbox)

def goal_track(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1 = x + int(w/2)
    c2 = y + int(h/2)
    cv2.circle(img,(c1,c2),2,(0,0,255),5)

    cv2.circle(img,(int(p1),int(p2)),2,(0,255,0),3)
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    print(dist)

    if(dist<=20):
        cv2.putText(img,"Objetivo",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs)-1):
        cv2.circle(img,(xs[i],ys[i]),2,(0,0,255),5)

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"Rastreando",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def goal_track(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])

while True:
   check,img = video.read()
   success,bbox = tracker.update(img)

   if success:
       drawBox(img,bbox)
   else:
       cv2.putText(img,"Perdido",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

   cv2.imshow("Resultado",img)

   key = cv2.waitKey(25)
   if key == 32:
       print("Termino de ejecucion")
       break

video.release()
cv2.destroyAllWindows() 
