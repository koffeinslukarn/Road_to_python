
from math import e
from signal import raise_signal
import lab5b


def test_pixelconstraint():
    '''Test if function gives right value for a fixed set of tests and condition'''
    test1 = [50, 50, 50]
    test2 = (0, 0, 0)
    test3 = (256, 100, 255)
    try:
        limit = lab5b.pixel_constraint(50, 255, 50, 255, 50, 255)
        lab5b.pixel_constraint(50, 256, 50, 255, 50, 255) 
        limit(test1)
        assert (limit(test2) == 0), "fel test2"
        assert (limit(test3) == 0), "fel test3"
        print("all test passed")
    except ValueError as e:
        assert str(e) == "ValueError, must be a valit hsv value"
    except TypeError as e:
        assert str(e) == "TypeError, Pixel must be a tuple"


def test_generator_from_image(img): 
    '''Tests if the right pixel is distrupited from function. A more generall test'''
    gen_result = lab5b.generator_from_image(img)
    try: 
        assert(gen_result(0) == (100, 100, 100))
        assert(gen_result(1) == (255, 255, 255))
        assert(gen_result(2) == (0,0,0))
        assert(gen_result(3) == (0, 0, 0))
        print("not passed all the test")
    except IndexError as e:
            assert str(e) == "Index out of range"
    return True


def test_combine_imgages():
    '''Test if the final and expected list is the same for a given list, condition and generators'''
    lst =  [(50, 100, 255), (200, 100, 255), (150, 150, 0)]
    lst2 =  (((50, 100, 255, 200, 100, 255, 150, 150, 0)))
    lst3 = ["hallå",(200, 100, 255), (150, 150, 0)]
    filt = lab5b.gradient_condition
    image1_lst = [(255, 255, 255), (128, 128, 128), (0, 0, 0)]
    image2_lst = [(255, 255, 255), (128, 128, 128), (128, 128, 128)]
    uneven_lst1 = [(255, 255, 255), (128, 128, 128), (0, 0, 0)]
    uneven_lst2 = [(255, 255, 255), (128, 128, 128)]
    try:
       gen1 = lab5b.generator_from_image(image1_lst)
       gen2 = lab5b.generator_from_image(image2_lst)
       gen3 = lab5b.generator_from_image(uneven_lst1)
       gen4 = lab5b.generator_from_image(uneven_lst2)
       test_result = lab5b.combine_images(lst, filt, gen1, gen2)
       lab5b.combine_images(lst2, filt, gen1, gen2)
       lab5b.combine_images(lst3, filt, gen1, gen2)
       lab5b.combine_images(lst, filt, gen3, gen4)

       assert (test_result == [(255, 255, 255),(128, 128, 128), (150, 150, 0)])
    except TypeError as e:
        assert str(e) == "wrong type of lst"
    except IndexError as e:
        assert str(e) == "Pictures must be same size"
    except ValueError as e:
       assert str(e) == "value from filt wrong"
    return True
    

def main_test():
    test_generator_from_image([(100, 100, 100), (255, 255, 255), (0, 0, 0)])
    test_pixelconstraint()
    test_combine_imgages()
    return "All tests passed"


print(main_test())

