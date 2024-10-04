import cv2
import numpy
import math

img = cv2.imread('skidsemester.JPG', 1)

def cvimg_to_list(picture):
   '''Convert BGR from picture to a list of tupels'''
   colourlist = []
   for y in range(picture.shape[0]):
       for x in range(picture.shape[1]):
           pixel = picture[y, x]
           new_tup = tuple(map(int, pixel))
           colourlist.append(new_tup)
   return colourlist


def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3d array that will contain the image data
    img = numpy.zeros((height, width, 3), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]

    return img

'''list_img = cvimg_to_list(img)
converted_img = rgblist_to_cvimg(list_img, img.shape[0], img.shape[1])
cv2.imshow("converted", converted_img)
cv2.waitKey(0) '''


def negative_gaus(x, y):
    '''Negative gaus blur'''
    result = (-1*(1/(2*math.pi*(4.5**2)))) * (math.e **(-1*((x**2 + y**2)/(2*4.5**2))))
    return result


def unsharp_mask(N):
    '''Creates a 2D list of NxN and use negative_gaus on each place'''
    '''Center value stays [1.5]'''
    filtered_position = []
    center = N // 2  
    for x in range(N):
        row = []  
        for y in range(N):
            if x == center and y == center:
                row.append([1.5])  
            else:
                row.append([negative_gaus(x - center, y - center)])  
        filtered_position.append(row)  
    
    return filtered_position


kernel = numpy.array(unsharp_mask(1000))
filtered_img = cv2.filter2D(img, -1, kernel)
cv2.imshow('orginal', img)
cv2.imshow("filtered", filtered_img)
cv2.waitKey(0)
