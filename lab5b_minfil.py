import cv2
import lab5a
import cvlib
import random


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    '''Return a function who shows if the pixel fits in the condition'''
    for value in (hlow, hhigh, slow, shigh, vlow, vhigh):
        if value < 0 or value > 255:
            raise ValueError("ValueError, must be a valit hsv value")
        elif not isinstance(value, int):
            raise SyntaxError("Invalid Syntax")
    def hsv_value(pixel):
        if not isinstance(pixel, tuple):
            raise TypeError(f"TypeError, Pixel must be a tuple, got {type(pixel)}")
        (h, s ,v) = pixel
        if hlow <= h <= hhigh and slow <= s <= shigh and vlow <= v <= vhigh:
            return 1
        else:
            return 0
    return hsv_value


'''hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
plane_list = lab5a.cvimg_to_list(hsv_plane)
is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)  # test första funktionen
sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))
cv2.imshow('sky', cvlib.greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
cv2.waitKey(0)'''


def generator_from_image(pic_list):
    '''From img list, returns img colour for a prefered index'''
    def list_to_index(i):
        if i >= len(pic_list):
            raise IndexError("Index out of range")
        else:
            return pic_list[i] 
    return list_to_index


'''orig_img = cv2.imread("plane.jpg")
orig_list = lab5a.cvimg_to_list(orig_img)
generator = generator_from_image(orig_list)
new_list = [generator(i) for i in range(len(orig_list))]  # test andra funtionen
cv2.imshow('original', orig_img)
cv2.imshow('new', cvlib.rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
cv2.waitKey(0)'''


def generator1(index):
    '''Geneates a random nightsky w stars'''
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)


def combine_images(lst, filt, gen1, gen2):
    """Takes in an image as a list and images hard or smooth """
    try:
       final_pic = []
       for i,elem in enumerate(lst):
           value = filt(elem)
           if value == 1:
            final_pic.append(gen1(i))
           elif value == 0:
            final_pic.append(gen2(i))
           else: final_pic.append(cvlib.add_tuples(cvlib.multiply_tuple(gen1(i), value), 
              cvlib.multiply_tuple(gen2(i), 1-value)))
    except IndexError:
        raise IndexError("Pictures must be same size")
    except TypeError:
        raise TypeError("wrong type of lst")
    except ValueError:
        raise ValueError("value from filt wrong")
    return final_pic


def gradient_condition(pixel):
    '''Returns a value between 1 and 0 from pixels hsv value'''
    return pixel[2] / 255


plane_img = cv2.imread('plane.jpg')
flower_img = cv2.imread('flower.jpg')   #påkallar bilder
greyscale_img = cv2.imread('greyscale.jpg')
condition = pixel_constraint(100, 150, 50, 200, 100, 255) #filter för himmelfärg
hsv_list = lab5a.cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
grey_scale_list = lab5a.cvimg_to_list(greyscale_img)
plane_list = lab5a.cvimg_to_list(plane_img)
flower_list = lab5a.cvimg_to_list(flower_img)    #påkallar listor för att användas i fuktioner
generator_plane = generator_from_image(plane_list)
generator_flower = generator_from_image(flower_list)
result2 = combine_images(grey_scale_list, gradient_condition, generator_flower, generator_plane)
result1 = combine_images(hsv_list, condition, generator1, generator_plane)

'''new_img = cvlib.rgblist_to_cvimg(result2, plane_img.shape[0], plane_img.shape[1]) # byt mellan result1 och 2 för att se båda testen.
cv2.imshow('Final image', new_img)
cv2.waitKey(0) '''
