import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.type_check import imag

def key_generator(img_row, img_col, key_str):
    key_str = key_str.replace(' ', '')
    len_key_str = len(key_str)
    
    key_array = np.zeros([img_row, img_col], dtype=np.uint8)
    
    for row in range(img_row):
        for col in range(img_col):
            key_array[row][col] = ((row*col)%len_key_str)
    
    Key = key_array*(2**8//(len_key_str))

    return Key

def XOR_Cypher(Img, Key):
    Img = plt.imread(Img)[:,:,:3]
   # new_image = np.bitwise_xor(Img, Key)
   # return new_image
    img_copy = np.copy(Img)
    row, col = Key.shape[0], Key.shape[1]

    for r in range(row):
        for c in range(col):
            #Key[row][col] = bin(Key[row][col])
            #Img[row][col] = bin(Img[row][col])
            Img[r][c] = Key[r][c] ^ Img[r][c]
    
    return Img

def main():
    phrase = 'COME AND GET YOUR LOVE'
    image = 'Pale_Blue_Dot_Encrypted.tiff'

    img = plt.imread(image)[:,:,:3]
    row = img.shape[0]
    column = img.shape[1]

    key = key_generator(row, column, phrase)
    pic = XOR_Cypher(image, key)
    plt.imsave("image.tiff", pic)


if __name__ == '__main__':
    main()