import cv2

# create a new cam object
cap = cv2.VideoCapture(0)
flame_cascade = cv2.CascadeClassifier("cascade_retrain_flame.xml")

while True:
    # read the image from the cam
    _, image = cap.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = flame_cascade.detectMultiScale(image_gray, 1.3, 5)
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
        cv2.putText(image,"Flame",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,2)
    print("No Flame")
    cv2.imshow("image", image)
    if len(faces) == 0:
        print("NO FLAME")
        continue
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
