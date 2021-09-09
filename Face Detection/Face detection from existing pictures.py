import cv2
# Creating a Cascade Classifer Object
face_cascade= cv2.CascadeClassifier("C:\\Users\\Aarshita Acharya\\anaconda3\\envs\\gest\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

# Reading the image, 1 means color, 0 means black and white
img = cv2.imread("C:\\Users\\Aarshita Acharya\\Downloads\\Aarshita.jpeg", 1)

# Reading the image as grayscale image
gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Searching for the coordinates of the image
# detectMultiScale is used to search for the face rectangle coordinates
# scaleFactor decreases the shape value by 5 % till the face is found
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors= 5)

print(type(faces))
print(faces)

# Method to create a face rectangle
# Green border and width 3
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

# Displaying the image
cv2.imshow("Profile", img)

# Waitkey 0 means the window closes after you press any key
cv2.waitKey(0)
cv2.destroyAllWindows()
