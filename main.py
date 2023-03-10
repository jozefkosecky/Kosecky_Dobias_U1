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
    frame = cv2.resize(frame, (250, 250))

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

dimensions = image1.shape

height, width, num_channels = image2.shape

rot_image = image2.copy()
for row in range(height):
         for col in range(width):
             rot_image[row][col], rot_image[col][row] = image2[col][row], image2[row][col]

red_image3 = image3.copy()
red_image3[:, :, 1:] = 0

# Concatenate the four images horizontally and vertically
top_row = np.concatenate((image1, rot_image), axis=1)
bottom_row = np.concatenate((red_image3, image4), axis=1)
concatenated_image = np.concatenate((top_row, bottom_row), axis=0)

# Create the sharpening kernel
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

# Apply the sharpening kernel to the image using filter2D
concatenated_image[0:dimensions[0], 0:dimensions[1]] = cv2.filter2D(concatenated_image[0:dimensions[0], 0:dimensions[1]], -1, kernel)

# Display the concatenated image with imshow
plt.imshow(concatenated_image)

# Save the concatenated image
cv2.imwrite("obrazok_final.jpg", concatenated_image)

# Print to terminal
h, w, n = concatenated_image.shape
print("datovy typ: " + str(concatenated_image.dtype))
print("rozmer: " + str(h) + str(w))
print("velkost obrazku: " + str(concatenated_image.size))

# Show the plot
plt.show()

cap.release()
cv2.destroyAllWindows()