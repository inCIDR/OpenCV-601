import cv2
import numpy as np

def Add_salt_pepper_noise(img,pa,pb):
     sp_noise =img.copy()
     amount1 = int(img.shape[0]*img.shape[1]*pa)
     amount2 = int(img.shape[0]*img.shape[1]*pb)
     
     for i in range(0,amount1):
     	sp_noise[int(np.random.uniform(0,img.shape[0])),int(np.random.uniform(0,img.shape[1]))] = 0
     for i in range(0,amount2):
     	sp_noise[int(np.random.uniform(0,img.shape[0])),int(np.random.uniform(0,img.shape[1]))] = 255

     return sp_noise

def Add_gaussian_noise(img,mean,sigma):
	NoiseArr = img.copy()
	cv2.randn(NoiseArr,mean,sigma)
	NoiseArr = cv2.add(img,NoiseArr)
	return NoiseArr

image = cv2.imread("Test_images/baboon.jpg", 0);
cv2.namedWindow( "Original image", cv2.WINDOW_NORMAL );
cv2.imshow( "Original image", image);

noise_img = image.copy();
mean = 0;
sigma = 60;
noise_img = Add_gaussian_noise(noise_img,mean,sigma);
cv2.imshow( "Gaussian Noise", noise_img);

noise_dst = noise_img.copy();
noise_dst = cv2.blur(noise_dst,(7,7));
cv2.imshow( "Box filter", noise_dst);

noise_dst1 = noise_img.copy()
noise_dst1 = cv2.GaussianBlur(noise_dst1, (7,7),1.5);
cv2.imshow( "Gaussian filter", noise_dst1);

noise_dst2 = noise_img.copy();
noise_dst2 = cv2.medianBlur(noise_dst2,7);
cv2.imshow( "Median filter", noise_dst2);

noise_img2 = image.copy()
pa = 0.1;
pb = 0.1;
noise_img2 = Add_salt_pepper_noise(noise_img2,pa,pb)
cv2.imshow( "Salt and Pepper Noise", noise_img2);

noise_dst3 = noise_img2.copy();
noise_dst3 = cv2.blur(noise_dst3,(7,7));
cv2.imshow( "Box filter SP", noise_dst3);

noise_dst4 = noise_img2.copy();
noise_dst4 = cv2.GaussianBlur(noise_dst4,(7,7),1.5);
cv2.imshow( "Gaussian filter SP", noise_dst4);

noise_dst5 = noise_img2.copy();
noise_dst5 = cv2.medianBlur(noise_dst5,7);
cv2.imshow( "Median filter SP", noise_dst5);

c = cv2.waitKey(0)