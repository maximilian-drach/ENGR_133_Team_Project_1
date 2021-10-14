import numpy as np
import matplotlib.pyplot as plt

img= input('Enter image file name: ')
if img.endswith('.jpg'):
    image = plt.imread(img)
elif img.endswith('.png'):
        image = plt.imread(img)
        image = (image*225).astype(np.unit8)
elif img.endswith('.tiff'):
    image = plt.imread(img)[:,:,:3]
 

   
image = plt.imread(img)
print(f'Dimensions of the image is {image.shape}') 
plt.imshow(image)

print(image)
    