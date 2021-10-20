import numpy as np
import matplotlib.pyplot as plt

def img_input():
    #gets file name
    img = input('Enter image file name: ')
    return img

def image_tester(img):
    #test the ending of the image file input 
    #then reads the file in correctly depending on the ending
    if img.endswith('.jpg'):
        image = plt.imread(img)
    elif img.endswith('.png'):
            image = plt.imread(img)
            image = (image*225).astype(np.unit8)
    elif img.endswith('.tiff'):
        image = plt.imread(img)[:,:,:3]
    else:
        image = False
 
    return image
   

def dim(image):
    #shows the dimension
    image = image_tester(image)
    dim = image.shape
    print(f'Dimensions of the image is {image.shape}')
    return dim
    
def main():
    pass

if __name__ == '__main__':
    main()