import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('image.tiff')[:,:,:3]
# plt.imshow(image)
grey=[]
g_row=[]
for row in image:
    for pixel in row:
        g_pix=[.2126*pixel[0],.7152*pixel[1],.0722*pixel[2]]
    grey.append(g_row)
    g_row=[]

plt.imshow(grey)



def float64_uint8(img):
    #gets the max number the data could be
    img_data_max = np.iinfo(img.dtype).max
    img = img.astype(np.float64)/img_data_max
    img = 255*img
    img = img.astype(np.uint8)

    return img