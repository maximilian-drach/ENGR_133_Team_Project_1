"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    Creates user functions to create a histogram showing the spread of red, green, and blue pixels in the image, generate a key for encrypting/decrypting an image (old method), and uses that key to encrypt/decrypt an image.

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
import key_generator as kg
import Image_analysis as ia

def histogram(image):
    #image = ia.image_tester(image)
    image=(image*255).astype(np.uint8)

    
    plt.hist(image[:,:,0].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='red', alpha=.1, label='Red Pixels')
    plt.hist(image[:,:,1].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='green', alpha=.1, label='Green Pixels')
    plt.hist(image[:,:,2].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='blue', alpha=.1, label='Blue Pixels')
    plt.legend()
    plt.show()
    
    

# #dont use this key, its not as good at encrypting
# def better_key(image, phrase):
#     phrase = phrase.replace(' ', '')
#     len_phrase = len(phrase)
    
#     np.random.seed(len_phrase)
    
#     img = plt.imread(image)[:,:,:3]
#     row = img.shape[0]
#     col = img.shape[1]
    
    
#     key = np.zeros([row,col], dtype=np.uint8)
    
#     for r in range(row):
#         for c in range(col):
#             key[r][c] = np.random.randint(0, high=266, size=None, dtype=int)
    
#     return key

            
#     # 1. get the length of the phrase
#     # 2. put the lenght into the rand seed
#     # 3. make the seed vales form 0-255
#     # 4. Xor the image
#     # 5. that encryotuion and do xor to decrypt
    


    
def pseudo_number_key(image, phrase):
    phrase = phrase.replace(' ', '')
    len_phrase = len(phrase)
    
    #creates the seed, by the length of the phrase
    seed = len_phrase*12345
    
    #loads the image dim
    #img = ia.image_tester(image)
    row = image.shape[0]
    col = image.shape[1]
    
    #Creates a new key array
    key = np.zeros([row,col], dtype=np.uint8)
    #creates the n0, n1, ...nx to make the series work
    num = seed
    
    for r in range(row):
        for c in range(col):
            num = ((1103515245*num) + seed)%(2**31)
            #loads the seed values into the array
            key[r][c] = num
            
    return key
    
def encrytion_image(image, phrase):
    key = pseudo_number_key(image, phrase)
    image = kg.XOR_Cypher(image, key)
    return image


def test():
    # image = input('Enter your image: ')
    # out_image = input('Enter your output image file (as a .tiff): ')
    # encrypt = bool(input('Is this an image encryption? enter(True or False): '))
    # if encrypt == True:
    #     phrase = input('Enter your encryption phrase: ')
    # else:
    #     phrase = input('Enter your decryption phrase: '))
    
    
    #image = 'try_this_image.tiff'
    image = ia.image_tester('image.tiff')
    #nKey = better_key(image, 'Test')
    nKey = pseudo_number_key(image, 'Test')
    encrypted_image = kg.XOR_Cypher(image, nKey)
    plt.imsave('encrypt.tiff', encrypted_image)
    pic = ia.image_tester('encrypt.tiff')
    histogram(pic)

    

    #encrypted = 'encrypt.tiff'
    #nKey = better_key(encrypted, 'Test')
    nKey = pseudo_number_key(pic, 'Test')
    image2 = kg.XOR_Cypher(pic, nKey)
    plt.imsave('orgin.tiff', image2)
    histogram(image2)
    

    

def main():
    
    test()
    #pass

if __name__ == '__main__':
    main()
    