import cv2
import os

while True:
    fileName = input("\nadd '.jpg' \nFile name: ")

    if os.path.exists(fileName):
        image = cv2.imread(fileName,1)
        cv2.imshow(fileName, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break

    else:
        print("File not found...")