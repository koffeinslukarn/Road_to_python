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
   


def negative_gaus(x, y):
    '''Negative gaus blur'''
    result = (-1*(1/(2*math.pi*(4.5**2)))) * (math.e **(-1*((x**2 + y**2)/(2*4.5**2))))
    return result


def unsharp_mask(N):
    '''Creates a 2D list of NxN and use negative_gaus on each place'''
    '''Center value stays [1.5]'''
    center = N // 2  
    filtered_position = [[1.5 if x == center and y == center else negative_gaus(x - center, y - center) for x in range(N)]
        for y in range(N)] 
    return filtered_position

