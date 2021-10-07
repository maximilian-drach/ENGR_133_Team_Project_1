import numpy as np
import matplotlib.pyplot as plt

def key_generator(img_row, img_col, key_str):
    key_str = key_str.replace(' ', '')
    len_key_str = len(key_str)
    
    key_array = [[0]*img_col]*img_row
    
    for row in range(img_row):
        for col in range(img_col):
            key_array[row][col] = ((row*col)%len_key_str)
    
    Key = key_array*(2**8//(len_key_str))

    return Key

def XOR_Cypher(Img, Key):
    row, col = Key.shape
    for row in range(row):
        for col in range(col):
            Key[row][col] = bin(Key[row][col])
            Img[row][col] = bin(Img[row][col])
            Img[row][col] = Key[row][col] ^ Img[row][col]
    
    return Img
