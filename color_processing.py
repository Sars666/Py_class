import cv2
import numpy

if __name__ == '__main__':
    img = cv2.imread("creeper.jpg")
    b, g, r = cv2.split(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print(b)