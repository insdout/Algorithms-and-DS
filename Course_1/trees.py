import math

class Node:
    def __init__(self, key=0, parent = None):
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
    pass

def check_BST(root):
    return _check_BST(root)[0]

def _min_diff(root):
    pass

def min_diff(root):
    return _min_diff(root)[0]

#################################################

if __name__ == "__main__":
    T = Node(3)
    insert(T, Node(6))
    insert(T, Node())

    # should print True
    #print(check_BST(T))
    # should print 1
    #print(min_diff(T))
    print(tree_max(Node()))
    print(tree_max(T))
    print(tree_size(T))
    print(tree_max(None))


