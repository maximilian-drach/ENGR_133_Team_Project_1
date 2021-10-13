import matplotlib.pyplot as plt

image = plt.imread('image.tiff')[:,:,:3]
# plt.imshow(image)
grey=[]
g_row=[]
for row in image:
    for pixel in row:
        g_row.append(.2126*pixel[0] + .7152*pixel[1] + .0722*pixel[2])