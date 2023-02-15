import cv2
import matplotlib.pyplot as plt
import numpy as np

import keyboard as keyboard

# create an instance of cv2.VideoCapture() to capture video from the default camera (notebook camera)
cap = cv2.VideoCapture(0)

# set the exposure, image format, and white balance of the camera (if applicable)
# you may need to adjust these settings based on your camera
cap.set(cv2.CAP_PROP_EXPOSURE, 0.1)
# cap.set(cv2.CAP_PROP_CONVERT_RGB, 0.1)
cap.set(cv2.CAP_PROP_AUTO_WB, 1)

counter = 0

while counter != 4:
    # capture a frame from the camera
    ret, frame = cap.read()

    # resize the frame (if desired)
    frame = cv2.resize(frame, (250, 250   ))

    # display the frame in a window
    cv2.imshow("test", frame)

    key = cv2.waitKey(1)

    if key == ord(' '):
        filename = "image{}.jpg".format(counter)
        cv2.imwrite(filename, frame)
        counter += 1
        print("Saved image to {}".format(filename))

    elif key == ord('q'):
        break


image1 = plt.imread("image0.jpg")
image2 = plt.imread("image1.jpg")
image3 = plt.imread("image2.jpg")
image4 = plt.imread("image3.jpg")

# Concatenate the four images horizontally and vertically
top_row = np.concatenate((image1, image2), axis=1)
bottom_row = np.concatenate((image3, image4), axis=1)
concatenated_image = np.concatenate((top_row, bottom_row), axis=0)

# Display the concatenated image with imshow
plt.imshow(concatenated_image)

# Show the plot
plt.show()
# release the camera and close the window
cap.release()
cv2.destroyAllWindows()