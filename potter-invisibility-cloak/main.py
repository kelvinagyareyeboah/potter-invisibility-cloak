

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
