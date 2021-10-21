# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:33:06 2021

@author: Maximilian_Drach_XPS
"""
import Histo_Key as hk
import key_generator as kg
import Image_analysis as ia
import main0 as m


def decrypt():
    image = input("Input your image infile (.tiff): ")
    out_image = input("Input your image outfile(.tiff): ")
    phrase = input("Input your decryption phrase: ")
    #nKey = hk.pseudo_number_key(image, phrase)
    pic = hk.encrytion_image(image, phrase)
    hk.plt.imsave(out_image, pic)
    hk.histogram(pic)

def encrypt():
    image = input("Input your plain image infile (.tiff): ")
    out_image = input("Input your encrypted image output file (.tiff): ")
    phrase = input("Input your decryption phrase: ")
    #nKey = hk.pseudo_number_key(image, phrase)
    pic =  hk.encrytion_image(image, phrase)
    hk.plt.imsave(out_image, pic)
    hk.histogram(pic)
def key():
    image = input("Input your plain image infile (.tiff): ")
    out_image = input("Input your encrypted image output file (.tiff): ")
    phrase = input("Input your decryption phrase: ")
    image = ia.image_tester(image)

    key = kg.key_generator(image, phrase)
    img = kg.XOR_Cypher(image, key)
    plt.imsave(out_image, img)
    
def main():
   decrypt()
   encrypt()

if __name__ == '__main__':
    main()
    



