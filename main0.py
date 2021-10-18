# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:08:12 2021

@author: Maximilian_Drach_XPS
"""

import Histo_Key as hk
import Image_analysis as ia
import grey_search as gs
import key_generator as kg


def main():
    image = input('Enter your image: ')
    out_image = input('Enter your output image file (as a .tiff): ')
    encrypt = bool(input('Is this an image encryption? enter(True or False): '))
    if encrypt == True:
        phrase = input('Enter your encryption phrase: ')
    else:
        phrase = input('Enter your decryption phrase: ')
    
    
    

    

if __name__ == '__main__':
    main()