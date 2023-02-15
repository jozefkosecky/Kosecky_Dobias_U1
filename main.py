import cv2

# create an instance of cv2.VideoCapture() to capture video from the default camera (notebook camera)
cap = cv2.VideoCapture(0)

# set the exposure, image format, and white balance of the camera (if applicable)
# you may need to adjust these settings based on your camera
cap.set(cv2.CAP_PROP_EXPOSURE, 0.1)
# cap.set(cv2.CAP_PROP_CONVERT_RGB, 0.1)
cap.set(cv2.CAP_PROP_AUTO_WB, 1)

while cv2.waitKey() != ord('q'):
    # capture a frame from the camera
    ret, frame = cap.read()

    # resize the frame (if desired)
    frame = cv2.resize(frame, (240, 240))

    # display the frame in a window
    cv2.imshow("test", frame)

# release the camera and close the window
cap.release()
cv2.destroyAllWindows()