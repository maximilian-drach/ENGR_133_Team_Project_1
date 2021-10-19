import numpy as np
import matplotlib.pyplot as plt

img= input('Enter image file name: ')

def image_tester(img):
    if img.endswith('.jpg'):
        image = plt.imread(img)
    elif img.endswith('.png'):
            image = plt.imread(img)
            image = (image*225).astype(np.unit8)
    elif img.endswith('.tiff'):
        image = plt.imread(img)[:,:,:3]
 
    return image
   
image = plt.imread(img)
def dim(image):
    print(f'Dimensions of the image is {image.shape}') 
    plt.imshow(image)

print(image)
    
def main():
    pass

if __name__ == '__main__':
    main()