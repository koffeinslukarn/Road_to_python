from lab7 import *
from lab7b import *

class TestTraverseFuntions(unittest.TestCase):
    def test_traverse(self):
        '''Test Traverse'''
        self.assertEqual(traverse([6, 7, 8], inner_node_fn, leaf_fn, empty_tree_fn), 43)
        '''test contains key'''
        self.assertTrue(contains_key(2, [6, 7, [[2, 3, 4], 0, []]]))
        self.assertFalse(contains_key(2, [[], 1, 5]))
        '''Tets tree size'''
        self.assertEqual(tree_size([2, 7, []]), 2)
        self.assertEqual(tree_size([]), 0)

        '''Test tree depth'''
        self.assertEqual(tree_depth(9), 1)
        self.assertEqual(tree_depth([1, 5, [10, 7, 14]]), 3)


#if __name__ == "__main__":
 #   unittest.main()


def test_search_and_match():
    '''Test if match funktion can return True or False
    and if search function returns correct book'''
    a_seq = ['a', ['b', ['c']]]
    a_pattern = ['a', 'b']  # false
    b_seq = ['j', 'b', 'c']
    b_pattern = ['&', 'b', 'c']  # true

    a_search_pattern = ['--', ['år', 1993], '--']
    b_search_pattern = [['författare', ['&', 'glenn', '&']], ['titel', ['--', 'science', '--']], ['år', '&']]
    search_seq = books.db
    c_search_pattern = []
    c_search_seq = []
    try:
        assert match(a_seq, a_pattern) == False, "fel a_match"
        assert match(b_seq, b_pattern) == True, "fel b_match"

        assert search(a_search_pattern, search_seq) == [[['författare', ['anders', 'haraldsson']],
                                                         ['titel', ['programmering', 'i', 'lisp']],
                                                         ['år', 1993]]], "fel a_search"

        assert search(b_search_pattern, search_seq) == [[['författare', ['j', 'glenn', 'brookshear']],
                                                         ['titel', ['computer', 'science', 'an', 'overview']],
                                                         ['år', 2011]]], "fel b_search"

        assert search(c_search_pattern, c_search_seq) == [], "fel c_search"
        print("All tests passed => test_search_and_match")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except SyntaxError as e:
        print(f"SyntaxError: {e}")


if __name__ == "__main__":
    test_search_and_match()
    unittest.main()
    #print("All tests passed => test_search_and_match")