import cv2
def nothing(x):
 pass
videoCapture = cv2.VideoCapture(0)
cv2.namedWindow('resultOfBnarization')
cv2.namedWindow('maskResultOfBnarization')
cv2.createTrackbar('minb', 'resultOfBnarization', 0, 255, nothing)
cv2.createTrackbar('ming', 'resultOfBnarization', 0, 255, nothing)
cv2.createTrackbar('minr', 'resultOfBnarization', 0, 255, nothing)
cv2.createTrackbar('maxb', 'resultOfBnarization', 0, 255, nothing)
cv2.createTrackbar('maxg', 'resultOfBnarization', 0, 255, nothing)
cv2.createTrackbar('maxr', 'resultOfBnarization', 0, 255, nothing)
while(True):
 _, frame = videoCapture.read();
 hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
 cv2.imshow('frame', hsv)
 minb = cv2.getTrackbarPos('minb', 'resultOfBnarization')
 ming = cv2.getTrackbarPos('ming', 'resultOfBnarization')
 minr = cv2.getTrackbarPos('minr', 'resultOfBnarization')
 maxb = cv2.getTrackbarPos('maxb', 'resultOfBnarization')
 maxg = cv2.getTrackbarPos('maxg', 'resultOfBnarization')
 maxr = cv2.getTrackbarPos('maxr', 'resultOfBnarization')
 hsv = cv2.blur(hsv,(5,5))
 mask = cv2.inRange(hsv, (minb, ming, minr), (maxb, maxg, maxr))
 cv2.imshow('maskResultOfBnarization', mask)
 result = cv2.bitwise_and(frame, frame, mask = mask)
 cv2.imshow('resultOfBnarization', result)
 if cv2.waitKey(1) == ord("q"):
    break
videoCapture.release()
cv2.destroyAllWindows()




target = cv2.imread('transition.jpg')
target = cv2.resize(target, (64, 64))
target = cv2.inRange(target, (56, 128, 188), (255, 255, 255))
cv2.imshow("Target image", target)
videoCapture = cv2.VideoCapture(0)
while (True):
 _,frame = videoCapture.read()
 cv2.imshow("Original Image", frame)
 frameForСutting = frame.copy()
 hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 hsvFrame = cv2.blur(hsvFrame, (5, 5))
 frameMask = cv2.inRange(hsvFrame, (56, 128, 188), (255, 255, 255))
 cv2.imshow("Frame mask", frameMask)
 frameMask = cv2.erode(frameMask, None, iterations=2)
 frameMask = cv2.dilate(frameMask, None, iterations=4)
 cv2.imshow("Smooth frame mask", frameMask)
 targetContours = cv2.findContours(frameMask, cv2.RETR_TREE,
cv2.CHAIN_APPROX_NONE)
 targetContours = targetContours[0]
 if targetContours:
  targetContours = sorted(targetContours, key=cv2.contourArea,
reverse=True)
  cv2.drawContours(frame, targetContours, 0, (0,0,255), 3)
  cv2.imshow("Contours of target", frame)
  (x,y, w, h) = cv2.boundingRect(targetContours[0])
  cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
  cv2.imshow("Rect on frame", frame)
  cuttingFrame = frameForСutting[y:y+h, x:x+w]
  cuttingFrame = cv2.resize(cuttingFrame, (64, 64))
  cuttingFrame = cv2.inRange(cuttingFrame, (56, 128, 188), (255, 255,
255))
 cv2.imshow("Current image", cuttingFrame)
 transitionCoincidence = 0
 for h in range(64):
  for w in range(64):
   if cuttingFrame[h][w] == target[h][w]:
    transitionCoincidence += 1
 if transitionCoincidence > 3100:
  print("Transition! Count of Coincidence ", transitionCoincidence)
 else:
  print("Nothing! Count of Coincidence ", transitionCoincidence)
 if cv2.waitKey(1) == ord("q"):
  break
videoCapture.release()
cv2.destroyAllWindows()


