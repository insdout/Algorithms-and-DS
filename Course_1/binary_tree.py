class Node():
    def __init__(self, value, parent=None):
        self.key = value
        self. parent = parent
        self.left = None
        self.right = None


def insert(root, node):
    if root.key > node.key:
        if root.left is None:
            root.left = node
            node.parent = root
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
            node.parent = root
        else:
            insert(root.right, node)


def inoder():
    pass



def postoder():
    pass




if __name__ == "__main__":
    T = Node(3)
    insert(T, Node(4))
    insert(T, Node(2))

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