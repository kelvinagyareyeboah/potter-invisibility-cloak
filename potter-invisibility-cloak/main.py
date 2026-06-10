
    # Segment imagesground, mask=mask)
    visible_area = cv2.bitwise_and(frame, frame, mask=invers
    output = cv2.add(cloak_area, visible_area)

    # Display resultoutput)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
