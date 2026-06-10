
    # Segment imagesground, mask=mask)
    visible_area_area)

    # Display resultoutput)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
