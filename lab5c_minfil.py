
from math import e
from signal import raise_signal
import lab5b


def test_pixelconstraint():
    '''Test if function gives right value for a fixed set of tests and condition'''
    test_1 = [50, 50, 50]
    test_2 = (0, 0, 0)
    test_3 = (256, 100, 255)
    try:
        limit = lab5b.pixel_constraint(50, 255, 50, 255, 50, 255)
        lab5b.pixel_constraint(50, 256, 50, 255, 50, 255) 
        limit(test_1)
        assert (limit(test_2) == 0), "fel test2"
        assert (limit(test_3) == 0), "fel test3"
        print("all test passed  =>test_pixelconstraint")
    except ValueError as e:
        assert str(e) == "ValueError, must be a valit hsv value"
        print(e, " =>test_pixelconstraint")
    except TypeError as e:
        assert str(e) == "TypeError, Pixel must be a tuple"
        print(e, " =>test_pixelconstraint")
        

def test_generator_from_image(img): 
    '''Tests if the right pixel is distrupited from function'''
    gen_result = lab5b.generator_from_image(img)
    try: 
        assert(gen_result(0) == (100, 100, 100))
        assert(gen_result(1) == (255, 255, 255))
        assert(gen_result(2) == (0,0,0))
        gen_result(3)
        print("passed all test generator  =>test_generator")
    except IndexError as e:
            assert str(e) == "Index out of range"
            print(e, " =>test_generator")
    

def test_combine_imgages():
    '''Test if the final and expected list is the same for a given list, condition and generators'''
    lst =  [(50, 100, 255), (200, 100, 255), (150, 150, 0)]
    lst_2 =  (((50, 100, 255, 200, 100, 255, 150, 150, 0)))
    lst_3 = ["hallå",(200, 100, 255), (150, 150, 0)]
    filt = lab5b.gradient_condition
    image_1_lst = [(255, 255, 255), (128, 128, 128), (0, 0, 0)]
    image_2_lst = [(255, 255, 255), (128, 128, 128), (128, 128, 128)]
    uneven_1_lst = [(255, 255, 255), (128, 128, 128), (0, 0, 0)]
    uneven_2_lst = [(255, 255, 255), (128, 128, 128)]
    try:
       gen_1 = lab5b.generator_from_image(image_1_lst)
       gen_2 = lab5b.generator_from_image(image_2_lst)
       gen_3 = lab5b.generator_from_image(uneven_1_lst)
       gen_4 = lab5b.generator_from_image(uneven_2_lst)
       test_result = lab5b.combine_images(lst, filt, gen_1, gen_2)
       lab5b.combine_images(lst_2, filt, gen_1, gen_2)
       lab5b.combine_images(lst_3, filt, gen_1, gen_2)
       lab5b.combine_images(lst, filt, gen_3, gen_4)
       assert (test_result == [(255, 255, 255),(128, 128, 128), (150, 150, 0)])
       print("all tests passed  =>test_combine")
    except TypeError as e:
        assert str(e) == "wrong type of lst"
        print(e," =>test_combine")
    except IndexError as e:
        assert str(e) == "Pictures must be same size"
        print(e, " =>test_combine")
    except ValueError as e:
       assert str(e) == "value from filt wrong"
       print(e, " =>test_combine")
    

if __name__ == "__main__":
    '''tests all the functions too see if all error where cought,
    and if all tests passed'''
    test_pixelconstraint()
    test_generator_from_image([(100, 100, 100), (255, 255, 255), (0, 0, 0)])
    test_combine_imgages()
    print("All errors cought by exceptions")
else:
    print("something wrong")
    






