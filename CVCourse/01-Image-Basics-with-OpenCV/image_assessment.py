import cv2
import numpy as np

img = cv2.imread('../DATA/dog_backpack.png')

def draw_circle(event,x,y,flags,params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),200,(255,0,0),20)
cv2.namedWindow(winname='dogpic')
cv2.setMouseCallback('dogpic',draw_circle)

while True:
    cv2.imshow('dogpic',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()