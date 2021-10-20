import numpy as np
import matplotlib.pyplot as plt
import scipy 


def img_input():
    #gets file name
    img = input('Enter image file name: ')
    return img

def image_tester(img):
    #test the ending of the image file input 
    #then reads the file in correctly depending on the ending
    if img.endswith('.jpg'):
        image = plt.imread(img)
    elif img.endswith('.png'):
            image = plt.imread(img)
            image = (image*225).astype(np.unit8)
    elif img.endswith('.tiff'):
        image = plt.imread(img)[:,:,:3]
    else:
        image = False
 
    return image
   

def dim(image):
    #shows the dimension
    image = image_tester(image)
    dim = image.shape
    print(f'Dimensions of the image is {image.shape}')
    return dim


def key_generator(img, key_str):
    
    key_str = key_str.replace(' ', '')
    len_key_str = len(key_str)
    
    img = image_tester(img) #plt.imread(img)[:,:,:3]
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
    Img = image_tester(Img) #plt.imread(Img)[:,:,:3]

    
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

def grey(image):
    
    image = image_tester(image)
    #uses matrix multiplication on the rgb values of the photo
    grey_values = (image[:,:,0]*.299 + image[:,:,1]*.587 + image[:,:,2]*.114)
    #this automatically gets the dim from the image, by just coppying
    grey = image.copy()
    
    #this inserts the grey rgb values in to the grey photo, since the rgb values should all the be same for the same row, col
    for i in range(3):
        grey[:,:,i] = grey_values

    return grey


def earth_finder(grey_image):
    #reads the string
    grey_image = image_tester(grey_image)
    
    #makes sure the border exception is taken out
    grey_image = grey_image[1:,1:,:]
    
    #gets the brighest spot on the image
    brightest_spot = np.amax(grey_image)
    
    #finds the index where the maximum value is
    index_max = np.where(grey_image == brightest_spot)
   
    #takes where first items(ie earth row, earth col) of each list return, the turns the tupple to a list
    cordinates = list(zip(index_max[0], index_max[1]))
   
    #since all rgb values are the same, we only need the first item of the list
    return cordinates[0]
    

def earth_image(grey_image):
    #gets the location
    location = earth_finder(grey_image)
    
    #it take the location and get the row-50 to row+50 and the same for the column with the color values the same
    grey_image = image_tester(grey_image)
    
    #gets the 101x101 image by take the place 0,0 as the location of the earth from the last fuction earth_finder
    #then is takes the 50 pixels, in front, above, behind and below it
    earth = grey_image[location[0]-50:location[0]+51, location[1]-50:location[1]+51,:]

    return earth

def image_smoother(image):
    image = image_tester(image)
    #using the guassian filter,  blurred the image
    blurred1 = scipy.ndimage.gaussian_filter(image, sigma=2.5)
    
    #gets the gradient of the blurred image in the x-direction
    sx = scipy.ndimage.sobel(blurred1, axis=0, output=None, mode ='constant', cval=0.0)
    #gets the gradient of the blurred image in the y-direction
    sy = scipy.ndimage.sobel(blurred1, axis=1, output=None, mode ='constant', cval=0.0)
    #hypot get the hypotenuse, or ie sqrt(a^2 + b^2) = C, this is get the gradient edge decetection
    #ie this combine the vertical and horizontal edges
    sob = np.hypot(sx, sy)
    
    return sob

def float64_uint8(img):
    #gets the max number the data could be
    #img_data_max = np.iinfo(img.dtype).max()
    #print(img_data_max)
    #img = img.astype(np.float64)/img_data_max
    img = image_tester(img)
    #times the image rgb value by 255 to get the unit8
    img = 255*img
    img = img.astype(np.uint8)

    return img


def uint8_float64(img):
    #img_data_max = np.iinfo(img.dtype).max
    img = image_tester(img)
    #dives the unint8 values to the get the 0-1 float64 values
    img = img/255
    img = img.astype(np.float64)

    return img

def histogram(image):
    image = image_tester(image)
    image=(image*255).astype(np.uint8)

    
    plt.hist(image[:,:,0].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='red', alpha=.1, label='Red Pixels')
    plt.hist(image[:,:,1].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='green', alpha=.1, label='Green Pixels')
    plt.hist(image[:,:,2].reshape(image.shape[0]*image.shape[1]),bins=np.arange(2**8+1), color='blue', alpha=.1, label='Blue Pixels')
    plt.legend()
    
    return plt.legend

def pseudo_number_key(image, phrase):
    phrase = phrase.replace(' ', '')
    len_phrase = len(phrase)
    
    #creates the seed, by the length of the phrase
    seed = len_phrase*12345
    
    #loads the image dim
    img = image_tester(image)
    row = img.shape[0]
    col = img.shape[1]
    
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