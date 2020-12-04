import cv2
import numpy as np

img1 = cv2.imread("mockup333.png")
img2 = cv2.imread("design3.png")
#img1 = cv2.imread("img11.png")
#img2 = cv2.imread("img22.png")
#img1 = cv2.imread("mockup11.png",-1)
#img2 = cv2.imread("mockup22.png",-1)
""" img1 = cv2.imread("mockup11.png")
img2 = cv2.imread("mockup22.png") """
#res =  img2 - img1
#ret,thresh1 = cv2.threshold(img2,0,255,cv2.THRESH_BINARY)

# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
# cv2.imshow("res", res)
#cv2.imshow("thresh1", thresh1)


""" bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2) """
_diff = cv2.absdiff(img2, img1)
cv2.imshow("PNG", _diff)

""" cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
#cv2.imwrite('messigray.png',bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2) """

tmp = cv2.cvtColor(_diff, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,5,255,cv2.THRESH_BINARY)
b, g, r = cv2.split(_diff)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba,4)
cv2.imwrite("test.png", dst)
cv2.imshow('PNG', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()