
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
