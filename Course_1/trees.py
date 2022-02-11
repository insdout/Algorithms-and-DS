# This assignment will consist of two parts. In the first, we will develop
# an algorithm to check whether a given binary tree has the BST property
# (we have carelessly relied on this in the lectures, it is time to check!).
# In the second part, we will see how some important operations that can be
# performed with sorted arrays efficiently can also be performed with BST's efficiently.
#
# We will aim at making the algorithms linear in the number of nodes in the tree.
# The algorithm below that computes the size of a binary tree is a template for all
# the problems in this assignment.
# Observe that the complexity of this algorithm is O(n), where nn is
# the number of nodes in a tree. Indeed, if we don't count the recursive calls,
# the complexity of the function is constant. Since we will call the function at
# most once for each node, we get O(n).
#
# Part 1. Write a function tree_max(T), where T is an instance of the Node
# class representing a binary tree (not necessarily a BST!), that find the largest
# number in the tree. For empty tree, we set the max to be -math.inf.
#
# Part 2. Write a function check_BST(T) (T is a binary tree as in Part
# 1) that returns True if T is a BST and False otherwise.
#
# Caveats:
#
# It is not enough to check that the key at each node is at most the key of the
# right child and at least the key of the left child. It has to be at most any key
# in the right subtree and at least any key in the left subtree.
#
# You might want to use the function tree_max from the Part 1 but this will
# likely damage your complexity.
#
# Hint: start with writing an auxiliary function _check_BST that will return a triple:
# whether the tree is BST or not, the minimum, and the maximum in the tree.
# Computing this function can be arranged in a similar fashion to tree_size.
#
# Part 3. Write a function min_diff(T) that takes as input a binary search tree T
# and computes the smallest absolute value of the difference between the keys in different nodes.
#
# Hint: start with an auxiliary function similarly to Part 2.
#
# Part 4. Write a function count_distinct(T) that takes as input a binary search tree T
# and computes the number of distinct keys present in the tree.
#
# Hint: again, start with a similar auxiliary function and the use the same strategy as tree_size.
#
# For all the parts, the number of nodes in the tree will be at most 200000.
# The time limit for each test will be one second.


import math


class Node:
    def __init__(self, key=0, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


def insert(root, node):
    if root.key > node.key:
        if root.left == None:
            root.left = node
            node.parent = root
        else:
            insert(root.left, node)
    else:
        if root.right == None:
            root.right = node
            node.parent = root
        else:
            insert(root.right, node)


#######################################################

def tree_size(root):
    if root is None:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)


def tree_max(root):
    if root is None:
        return -math.inf
    return max(root.key, tree_max(root.left), tree_max(root.right))


def _check_BST(root):
    if root is None:
        return None, None, True
    left_min, left_max, is_bst_left = _check_BST(root.left)
    right_min, right_max, is_bst_right = _check_BST(root.right)
    if right_max is None and right_min is None:
        right_max = right_min = root.key
    if left_max is None and left_min is None:
        left_max = left_min = root.key
    return min(root.key, left_min, right_min), \
        max(root.key, left_max, right_max), \
        (left_max <= root.key <= right_min) and is_bst_left and is_bst_right


def check_BST(root):
    return _check_BST(root)[2]


def _min_diff(root):
    pass


def min_diff(root):
    return _min_diff(root)[0]


#################################################

if __name__ == "__main__":
    T = Node(3)
    insert(T, Node(6))
    insert(T, Node(2))
    insert(T, Node(-7))
    insert(T, Node(-1))
    # T.right.key = -12
    # should print True
    # print(check_BST(T))
    # should print 1
    # print(min_diff(T))
    import binarytree


    def convert_to_bintree(root):
        new_root = binarytree.Node(root.key)
        if root.left != None:
            new_root.left = convert_to_bintree(root.left)
        if root.right != None:
            new_root.right = convert_to_bintree(root.right)
        return new_root


    def print_tree(root):
        print(convert_to_bintree(root))


    print_tree(T)
    print(tree_max(Node()))
    print(tree_max(T))
    print(tree_size(T))
    print(_check_BST(T))
    print(tree_max(None))
