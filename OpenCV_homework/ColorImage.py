import cv2
import sys

src = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR);
cv2.namedWindow( "Original image", cv2.WINDOW_NORMAL );
cv2.imshow( "Original image", src);

print (src[25,20])
red,green,blue = cv2.split(src)
'''
red = src.copy()
red[:, :, 1] = 0
red[:, :, 2] = 0

green = src.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

blue = src.copy()
blue[:, :, 1] = 0
blue[:, :, 0] = 0
'''
cv2.imshow("red",red)
cv2.imshow("green",green)
cv2.imshow("blue",blue)


imgYCC = cv2.cvtColor(src, cv2.COLOR_BGR2YCR_CB)
Y,Cb,Cr = cv2.split(imgYCC)
cv2.imshow("Y",Y)
cv2.imshow("Cb",Cb)
cv2.imshow("Cr",Cr)
print (imgYCC[25,20])

imgHSV = cv2.cvtColor(src, cv2.COLOR_RGB2HSV)
H,S,V = cv2.split(imgHSV)
cv2.imshow("H",H)
cv2.imshow("S",S)
cv2.imshow("V",V)
print (imgHSV[25,20])

c = cv2.waitKey(0)