import cv2

print("Printing Weird Childe...")

filePath = 'childe.jpg'
img = cv2.imread(filePath, 1)
cv2.imshow("Childe", img)
cv2.waitKey(0)
cv2.destroyAllWindows()