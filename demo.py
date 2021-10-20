# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:33:06 2021

@author: Maximilian_Drach_XPS
"""
import Histo_Key as hk
import key_generator as kg


def decrypt():
    image = input("Input your image infile (.tiff): ")
    out_image = input("Input your image outfile(.tiff): ")
    phrase = input("Input your decryption phrase: ")
    nKey = hk.pseudo_number_key(image, phrase)
    pic = kg.XOR_Cypher(image, nKey)
    hk.plt.imsave(out_image, pic)
    hk.histogram(pic)

def encrypt():
    image = input("Input your plain image infile (.tiff): ")
    out_image = input("Input your encrypted image output file (.tiff): ")
    phrase = input("Input your decryption phrase: ")
    nKey = hk.pseudo_number_key(image, phrase)
    pic = kg.XOR_Cypher(image, nKey)
    hk.plt.imsave(out_image, pic)
    hk.histogram(pic)

def main():
   decrypt()
   #encrypt()

if __name__ == '__main__':
    main()
    



