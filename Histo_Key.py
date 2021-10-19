

import numpy as np
import matplotlib.pyplot as plt
import key_generator as kg

def histogram(image):
    
    image=(image*255).astype(np.uint8)

    
    plt.hist(image[:,:,0].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='red', alpha=.1, label='Red Pixels')
    plt.hist(image[:,:,1].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='green', alpha=.1, label='Green Pixels')
    plt.hist(image[:,:,2].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='blue', alpha=.1, label='Blue Pixels')
    plt.legend()
    
    return plt.legend
   
    
    
 

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
    


    
def use_key(image, phrase):
    phrase = phrase.replace(' ', '')
    len_phrase = len(phrase)
    
    seed = len_phrase*12345
    
    img = plt.imread(image)[:,:,:3]
    row = img.shape[0]
    col = img.shape[1]
    
    
    key = np.zeros([row,col], dtype=np.uint8)
    num = seed
    
    for r in range(row):
        for c in range(col):
            num = ((1103515245*num) + seed)%(2**31)
            key[r][c] = num
            
    return key
    
    


def test():
    # image = input('Enter your image: ')
    # out_image = input('Enter your output image file (as a .tiff): ')
    # encrypt = bool(input('Is this an image encryption? enter(True or False): '))
    # if encrypt == True:
    #     phrase = input('Enter your encryption phrase: ')
    # else:
    #     phrase = input('Enter your decryption phrase: '))
    
    
    
    #image = 'try_this_image.tiff'
    image = 'image.tiff'
    #nKey = better_key(image, 'Test')
    nKey = use_key(image, 'Test')
    pic = kg.XOR_Cypher(image, nKey)
    plt.imsave('encrypt.tiff', pic)
    pic = plt.imread('encrypt.tiff')[:,:,:3]
    histogram(pic)

    

    encrypted = 'encrypt.tiff'
    #nKey = better_key(encrypted, 'Test')
    nKey = use_key(encrypted, 'Test')
    image2 = kg.XOR_Cypher(encrypted, nKey)
    plt.imsave('orgin.tiff', image2)
    #histogram(image2)
    
def main():
    
    test()
    #pass

if __name__ == '__main__':
    main()
    