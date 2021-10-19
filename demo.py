# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:33:06 2021

@author: Maximilian_Drach_XPS
"""
import Histo_Key as hk
import Image_analysis as ia
import grey_search as gs
import key_generator as kg


#image = input("Input the encrypted image (.tiff): ")
image = 'try_this_image.tiff'
phrase = 'Test Image in Class'
nKey = hk.use_key(image, phrase)
pic = kg.XOR_Cypher(image, nKey)
hk.plt.imsave('LC5_07_Image1.tiff', pic)
pic = hk.plt.imread('LC5_07_Image1.tiff')[:,:,:3]
hk.histogram(pic)



# encrypted = 'encrypt.tiff'
# nKey = hk.use_key(encrypted, 'Test')
# image2 = kg.XOR_Cypher(encrypted, nKey)
# plt.imsave('orgin.tiff', image2)
# #histogram(image2)