import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img = img[:,:,0].copy()
h,w = img.shape

for i in range(0,h):
    for j in range(0,w):
        img[i][j] = img[i][j]+0.1
print(img)
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img, cmap="gray")

img_rot = np.zeros((w,h))
for i in range (0,h):
    img_rot[:,h-1-i] = img[i,:]

#imgrot90 = np.rot90(img)

img_mirror = np.zeros((w,h))
for i in range (w):
    img_mirror[w-1-i,:]= img_rot[i,:]
scaling_factor = 10
img_resized = np.zeros((w//scaling_factor,h//scaling_factor))
for i in range(w):
    for j in range(h):
        i_resized = i // scaling_factor
        j_resized = j // scaling_factor
        if (i + scaling_factor) % 10 == 0 and (j + scaling_factor) % 10 == 0:
            img_resized[i_resized,j_resized]= img_mirror[i,j]


img_second_forth = np.zeros((h,w))
for i in range(h):
    for j in range(w):
        if 240 <= j < 480:
            img_second_forth[i,j]=img[i,j]


plt.figure()
plt.imshow(img_rot,cmap="gray")
plt.figure()
plt.imshow(img_mirror, cmap="gray")   
plt.figure()
plt.imshow(img_resized,cmap ="gray")
plt.figure()
plt.imshow(img_second_forth, cmap="gray")
plt.show()