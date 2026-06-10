import cv2
impor
#
cam = cv2.Vi
if n
    print("Error: Could not access webcam.")
    exit()

# Captur
for _ in range(30):
    success, background = 

if not success:
    print("Failed to capture background.")
    cam.release()
    exit()

background = cv2.flip(background, 1)
print("Background Captured Successfully!")

# Morphological kernel
kernel = np.ones((3, 3), np.uint8)

while True:
    success, frame = cam.read()

    if not success:
        print("Failed to read frame.")
        break

    # Flip frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Green color range
    lower_green = np.array([50, 80, 50])
    upper_green = np.array([90, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Noise removal
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)

    # Inverse mask
    inverse_mask = cv2.bitwise_not(mask)

    # Segment images
    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    visible_area = cv2.bitwise_and(frame, frame, mask=inverse_mask)

    # Final output
    output = cv2.add(cloak_area, visible_area)

    # Display result
    cv2.imshow("Magic Cloak", output)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
