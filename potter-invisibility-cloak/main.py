
nd... Please move out of the frame.")

# =========================
# Ca
        contin
    if background is None:
        background = frame.astype(float)
    else:
        cv2.accumulateWeighted(frame, background, 0.1)

background = cv2.convertScaleAbs(background)

print("Background captured successfully!")
print("Wear a GREEN cloth and enjoy the invisibility effect.")
print("Press 'q' to quit.")

# =========================
# Morphological Kernels
# =========================
kernel_open = np.ones((5, 5), np.uint8)
kernel_close = np.ones((7, 7), np.uint8)

# FPS Variables
prev_time = time.time()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # ==================================
    # Convert BGR → HSV
    # ==================================
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ==================================
    # Green Color Detection
    # ==================================
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([90, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    # ==================================
    # Noise Reduction
    # ==================================
    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel_open,
        iterations=2
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel_close,
        iterations=2
    )

    # Smooth mask edges
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    inverse_mask = cv2.bitwise_not(mask)

    # ==================================
    # Create Invisible Effect
    # ==================================
    cloak = cv2.bitwise_and(background, background, mask=mask)

    visible = cv2.bitwise_and(frame, frame, mask=inverse_mask)

    output = cv2.addWeighted(cloak, 1, visible, 1, 0)

    # ==================================
    # FPS Counter
    # ==================================
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(
        output,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        output,
        "Press Q to Quit",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # ==================================
    # Display Windows
    # ==================================
    cv2.imshow("Magic Cloak", output)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        break

# =========================
# Cleanup
# =========================
cap.release()
cv2.destroyAllWindows()
