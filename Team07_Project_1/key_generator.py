"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    Creates user functions that handle generating encryption key and using the encryption key to encrypt or decrypt an image.

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
import Image_analysis as ia


def key_generator(img, key_str):
    
    key_str = key_str.replace(' ', '')
    len_key_str = len(key_str)
    
    #img = ia.image_tester(img) #plt.imread(img)[:,:,:3]
    #gets the dimensions of the image
    row = img.shape[0]
    col = img.shape[1]
    
    #creates hte new array
    key_array = np.zeros([row, col], dtype=np.uint8)
    
    #loads the key values into the key array
    for r in range(row):
        for c in range(col):
            key_array[r][c] = ((r*c)%len_key_str)
    
    Key = key_array*(2**8//(len_key_str))

    return Key
def XOR_Cypher(Img, Key):
    
    #reads the image
    #Img = ia.image_tester(Img) #plt.imread(Img)[:,:,:3]

    
    #is a quicker way to encrypt the iage
    for i in range(3):
        #the i is the color channels to encrypt
        #the np.bitwise converts to bit then takes the xor operator by dot properties
        Img[:,:,i] = np.bitwise_xor(Img[:,:,i], Key)
    
    return Img
     # new_image = np.bitwise_xor(Img, Key)
     # return new_image
     # img_copy = np.copy(Img)
     # row, col = Img.shape[0], Img.shape[1]
    
      # for r in range(row):
      #     for c in range(col):
      #         #Key[row][col] = bin(Key[row][col])
      #         #Img[row][col] = bin(Img[row][col])
      #         Img[r][c] = Key[r][c] ^ Img[r][c]


def test():
    phrase = 'COME AND GET YOUR LOVE'
    img = 'Pale_Blue_Dot_Encrypted.tiff'

    img = ia.image_tester(img)
    

    key = key_generator(img, phrase)

    print(key)
    pic = XOR_Cypher(img, key)
    plt.imsave("image.tiff", pic)

def main():
    test()

if __name__ == '__main__':
     main()