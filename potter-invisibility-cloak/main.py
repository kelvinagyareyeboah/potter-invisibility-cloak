import cv2
import numpy as np

cam = cv2.VideoCapture(0)

for i in range(30):
    status, background = cam.read()

if not status:
    print("Failed to capture background.")
    cam.release()
    exit()

background = np.flip(background, axis=1)
print("Background Captured...")

while cam.isOpened():
    return_val, img = cam.read()
    if not return_val:
        break

    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([50, 80, 50])
    upper_green = np.array([90, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

    cloth = cv2.bitwise_and(background, background, mask=mask)
    inverse_mask = cv2.bitwise_not(mask)
    current = cv2.bitwise_and(img, img, mask=inverse_mask)
    combined = cv2.add(cloth, current)

    cv2.imshow("Magic Happens Here", combined)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
