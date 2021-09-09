import cv2, time

# 0 specifies using the inbuilt camera, or you can also add path for your video
# For external cam we can use 1, if 2 external cams: to use third one type 2 and so on
video = cv2.VideoCapture(0,  cv2.CAP_DSHOW)

a= 1
while True:
    a = a + 1
    # Check is a boolean data type which will return true if Python is able to read the video capture
    # Frame is a numpy array, it represents the first image that video captures.
    check, frame =video.read()
    print(frame)

    # Convert to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    cv2.imshow('Capture', frame)
    # This will generate a new frame every 1 milli second
    key = cv2.waitKey(1)

    # Once you enter q, entire window is destroyed
    if key == ord('q'):
        break

print(a)
# To release the camera in milli seconds
video.release()
cv2.destroyAllWindows()
