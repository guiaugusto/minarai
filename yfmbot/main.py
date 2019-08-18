import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('screen.jpg', cv2.IMREAD_UNCHANGED)
zoa_card = cv2.imread('zoa.png', cv2.IMREAD_UNCHANGED)

# img_ar = np.asarray(img)

counter = 0

# for pixel in img:
#     counter+=1

# for pixel in img:
#     for i in pixel:
#         print(len(i))
#         break
#     break

# for pixel in zoa_card:
#     print(len(pixel))
#     counter+=1

# for pixel in img:
#     if pixel in zoa_card:
#         counter+=1
img = img[228:276,30:90,::-1]
img = cv2.resize(img, (zoa_card.shape[1], zoa_card.shape[0]), 0, 0, cv2.INTER_NEAREST)

# print(counter)

# cv2.imshow('image', img)
# cv2.imshow('image', zoa_card)
# cv2.waitKey(10000)

# print(len(img))

# plt.imshow(img)
plt.imshow(zoa_card[:,:,::-1])
plt.plot([],[])
plt.show()
