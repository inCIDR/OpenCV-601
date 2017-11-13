import cv2

def Add_salt_pepper_noise(img,pa,pb):
	RNG rng; // rand number generate
    int amount1=srcArr.rows*srcArr.cols*pa; //Need to run through all channels
    int amount2=srcArr.rows*srcArr.cols*pb;
    for(int counter=0; counter<amount1; ++counter)
    {
     srcArr.at<uchar>(rng.uniform( 0,srcArr.rows), rng.uniform(0, srcArr.cols)) =0;

    }
     for (int counter=0; counter<amount2; ++counter)
     {
     srcArr.at<uchar>(rng.uniform(0,srcArr.rows), rng.uniform(0,srcArr.cols)) = 255;
     }

def Add_gaussian_noise(img,mean,sigma):
    Mat NoiseArr = srcArr.clone();
    RNG rng;
    rng.fill(NoiseArr, RNG::NORMAL, mean,sigma);  
    add(srcArr, NoiseArr, srcArr);  

image = cv2.imread("Test_images/baboon.jpg", 0);
cv2.namedWindow( "Original image", cv2.WINDOW_NORMAL );
cv2.imshow( "Original image", image);

noise_img = image.clone();
mean = 0;
sigma = 50;
Add_gaussian_noise(noise_img,mean,sigma);
cv2.imshow( "Gaussian Noise", noise_img);

noise_dst = noise_img.clone();
cv2.blur(noise_dst,noise_dst,cv2.Size(3,3));
cv2.imshow( "Box filter", noise_dst);

noise_dst1 = noise_img.clone()
cv2.GaussianBlur(noise_dst1, noise_dst1, cv2.Size(3,3),1.5);
cv2.imshow( "Gaussian filter", noise_dst1);

noise_dst2 = noise_img.clone();
cv2.medianBlur(noise_dst2,noise_dst2,3);
cv2.imshow( "Median filter", noise_dst2);

noise_img2 = image.clone()
pa = 0.01;
pb = 0.01;
Add_salt_pepper_noise(noise_img2,pa,pb)
cv2.imshow( "Salt and Pepper Noise", noise_img2);

noise_dst3 = noise_img2.clone();
cv2.blur(noise_dst3,noise_dst3,cv2.Size(3,3));
cv2.imshow( "Box filter", noise_dst3);

noise_dst4 = noise_img2.clone();
cv2.GaussianBlur(noise_dst4,noise_dst4,cv2.Size(3,3),1.5);
cv2.imshow( "Gaussian filter", noise_dst4);

noise_dst5 = noise_img2.clone();
cv2.medianBlur(noise_dst5,noise_dst5,3);
cv2.imshow( "Median filter", noise_dst5);