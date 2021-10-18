

import numpy as np
import matplotlib.pyplot as plt
import key_generator_team07 as kg

def histogram(image):
    image=(image*255).astype(np.uint8)
    
    plt.hist(image[:,:,0].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='red', alpha=.5, label='Red Pixels')
    plt.hist(image[:,:,1].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='green', alpha=.5, label='Green Pixels')
    plt.hist(image[:,:,2].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='blue', alpha=.5, label='Blue Pixels')
    plt.legend()
    
    return plt.legend
  

def better_key(image, phrase):
    phrase = phrase.replace(' ', '')
    len_phrase = len(phrase)
    
    np.random.seed(len_phrase)
    
    img = plt.imread(image)[:,:,:3]
    row = img.shape[0]
    col = img.shape[1]
    
    
    key = np.zeros([row,col], dtype=np.uint8)
    
    for r in range(row):
        for c in range(col):
            key[r][c] = np.random.randint(0, high=266, size=None, dtype=int)
    
    return key

            
    # 1. get the length of the phrase
    # 2. put the lenght into the rand seed
    # 3. make the seed vales form 0-255
    # 4. Xor the image
    # 5. that encryotuion and do xor to decrypt
    

# def seed_func(si, s0):
    
# def use_key(image, phrase):
#     phrase = phrase.replace(' ', '')
#     len_phrase = len(phrase)
    
#     seed = len_phrase
    
#     img = plt.imread(image)[:,:,:3]
#     row = img.shape[0]
#     col = img.shape[1]
    
    
#     key = np.zeros([row,col], dtype=np.uint8)
    
#     for r in range(row):
#         for c in range(col):
            
    
    
#image = plt.imread('Pale_Blue_Dot_Encrypted.tiff')[:,:,:3]
#key = kg.key_generator(image, 'COME AND GET YOUR LOVE')
#pic = kg.XOR_Cypher(img, key)


def test():
    imag = plt.imread('Pale_Blue_Dot_Encrypted.tiff')[:,:,:3]
    histogram(imag)
    
    
    image = 'image.tiff'
    nKey = better_key(image, 'Test')
    pic = kg.XOR_Cypher(image, nKey)
    plt.imsave('encypt.tiff', pic)
    
    

    encrypted = 'encypt.tiff'
    nKey = better_key(encrypted, 'Test')
    image2 = kg.XOR_Cypher(encrypted, nKey)
    plt.imsave('orgin.tiff', image2)
    
def main():
    pass

if __name__ == '__main__':
    main()
    