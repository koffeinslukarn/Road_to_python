import unittest


def is_empty_tree(tree):
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    return isinstance(tree, int)



def left_subtree(tree):
    return tree[0]



def right_subtree(tree):
    return tree[2]


def empty_tree_fn():
    return False


def leaf_fn(key):
    return key**2


def inner_node_fn(key, left_value, right_value):
    return key + left_value


def traverse(tree, inner_node, leaf, empty_tree):
    """Function to traverse a tree"""
    if is_empty_tree(tree):
        return empty_tree()
    elif is_leaf(tree):
        return leaf(tree)
    else:
        left = traverse(left_subtree(tree), inner_node, leaf, empty_tree)
        right = traverse(right_subtree(tree), inner_node, leaf, empty_tree)
        return inner_node(tree[1], left, right)

def traverse_value(tree):
    """Function to return the value of a tree"""
    def empty_tree_fn():
        return 0

    def leaf_fn(key):
        return key ** 2

    def inner_node_fn(key, left_value, right_value):
        return key + left_value
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def contains_key(search_key, tree):
    """Function to check if a tree contains a key"""
    def empty_tree_tf():
        '''If empty tree returns false'''
        return False
    
    def leaf_tf(leaf):
        '''If search_key match leif returns True else False'''
        return leaf == search_key
    
    def inner_node_tf(key, left_value, right_value):
        '''Inner node that retuerns true if search_key has same value in the list'''
        return key == search_key or left_value or right_value
    is_key_in_tree = traverse(tree, inner_node_tf, leaf_tf, empty_tree_tf)

    return is_key_in_tree


def tree_size(tree):
    """Function to return the size of a tree"""
    def empty_tree_l():
        return 0
    def leaf_l(leaf):
        return 1
    def inner_node_l(tree, left_size, right_size):
        return 1 + left_size + right_size
    return traverse(tree, inner_node_l, leaf_l, empty_tree_l)


def tree_depth(tree):
    """Function to calculate the depth of a tree."""
    def empty_tree_fn():
        return 0
    
    def leaf_fn(leaf):
        return 1
    
    def inner_node_fn(tree, left_depth, right_depth):
        return 1 + max(left_depth, right_depth)
    
    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)
