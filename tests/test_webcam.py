import numpy as np
import cv2
import time
import pandas as pd

CV_CAP_PROP_FRAME_WIDTH = 3
CV_CAP_PROP_FRAME_HEIGHT = 4
CV_CAP_PROP_BUFFERSIZE = 18

cap = cv2.VideoCapture(0)
cap.set(CV_CAP_PROP_BUFFERSIZE, 3)
# cap.set(CV_CAP_PROP_FRAME_WIDTH, 100)
# cap.set(CV_CAP_PROP_FRAME_HEIGHT, 10)
cap.set(3, 640)
cap.set(4, 480)
# cap.set(3, 1280)
# cap.set(4, 720)
i = 0
ts = {'read': [], 'show': [], 'wait': []}
while(True):
    # Capture frame-by-frame
    print('Frame: ' + str(i))
    i += 1

    t = time.time()
    ret, frame = cap.read()
    dt = time.time() - t
    print('  read: %2.4f' % float(dt))
    ts['read'].append(dt)
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    t = time.time()
    cv2.imshow('frame', frame)
    dt = time.time() - t
    print('  show: %2.4f' % float(dt))
    ts['show'].append(dt)
    # cv2.imshow('frame',gray)

    t = time.time()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        dt = time.time() - t
        print('  wait: %2.4f' % float(dt))
        ts['wait'].append(dt)
        break
    dt = time.time() - t
    print('  wait: %2.4f' % float(dt))
    ts['wait'].append(dt)

df = pd.DataFrame(ts)
# # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()