 import cv2
 import matplotlib.pyplot as plt
 
 src = cv2.imread('../1.png')
 
 dst = cv2.edgePreservingFilter(src, flags=1, sigma_s=60, sigma_r=0.4)
 
 dst = cv2.detailEnhance(src, sigma_s=10, sigma_r=0.15)
 
 dst_gray, dst_color = cv2.pencilSketch(src, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
 
 dst = cv2.stylization(src, sigma_s=60, sigma_r=0.07)
 
 plt.imshow(src)
