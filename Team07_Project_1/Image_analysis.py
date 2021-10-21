"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    Creates user functions to get the filename of an image, check if the filename is a valid image format, reading an image depending on its type, and finding the dimensions of an image.

Assignment Information
    Assignment:     Group Project
    Author:         David Gedgaud, dgedgaud@purdue.edu
                    Connor Gass, gass0@purdue.edu
                    Ashwin Limaye, limaye@purdue.edu
                    Max Drach, mdrach@purdue.edu
                    
    Team ID:        LC5 - 07

Contributor:    Name, login@purdue [repeat for each]
    My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

def img_input():
    #gets file name
    img = input('Enter image file name: ')
    return img

def image_valid(img):
    if img.endswith('.jpg'):
        image = True
    elif img.endswith('.png'):
        image = True
    elif img.endswith('.tiff'):
        image = True
    else:
        image = False
 
    return image

def image_tester(img):
    #test the ending of the image file input 
    #then reads the file in correctly depending on the ending
    if img.endswith('.jpg'):
        image = plt.imread(img)
    elif img.endswith('.png'):
        image = plt.imread(img)
        image = image.astype(np.uint8)
    elif img.endswith('.tiff'):
        image = plt.imread(img)[:,:,:3]
        
    return image
   

def dim(image):
    #shows the dimension
    #image = image_tester(image)
    dim = image.shape
    print(f'Dimensions of the image is {image.shape}')
    return dim
    
def test():
    image = image_tester('image.tiff')
    dim(image)

def main():
    test()

if __name__ == '__main__':
    main()