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
    bst_left_min, bst_left_max, is_bst_left = _check_BST(root.left)
    bst_right_min, bst_right_max, is_bst_right = _check_BST(root.right)
    if bst_right_max is None and bst_right_min is None:
        bst_right_max = bst_right_min = root.key
    if bst_left_max is None and bst_left_min is None:
        bst_left_max = bst_left_min = root.key
    return min(root.key, bst_left_min, bst_right_min), \
        max(root.key, bst_left_max, bst_right_max), \
        (bst_left_max <= root.key <= bst_right_min) and is_bst_left and is_bst_right


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
