# Given the head of a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which
# the depth of the two subtrees of every node never differ by more than 1.
#
#
#
# Example 1:
#
#
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
# Example 2:
#
# Input: head = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in head is in the range [0, 2 * 104].
# -105 <= Node.val <= 105


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node
    def __repr__(self):
        l = [self.val]
        node = self.next
        while node:
            l.append(node.val)
            node = node.next
        return str(l)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values is not None:
            self.insert(values)

    def insert(self, values):
        for val in values:
            node = self.head
            if not node:
                self.head = ListNode(val)
            else:
                while node.next:
                    node = node.next
                node.next = ListNode(val)

    def __repr__(self):
        str_repr = []
        node = self.head
        while node:
            str_repr.append(node.val)
            node = node.next
        return str(str_repr)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import binarytree


def convert_to_bintree(root):
    new_root = binarytree.Node(root.val)
    if root.left != None:
        new_root.left = convert_to_bintree(root.left)
    if root.right != None:
        new_root.right = convert_to_bintree(root.right)
    return new_root


def print_tree(root):
    print(convert_to_bintree(root))


def sortedListToBST(head):
    def find_mid(start):
        slow = start
        fast = start
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return slow, prev
    def get_bst(head):
        if not head:
            return None
        left = head
        print("=============")
        print("call", head)
        mid, prev = find_mid(head)
        print("mid", mid, "prev:", prev)

        root = TreeNode(mid.val)
        if not prev:
            print("not prev", mid, prev)
            return root
        else:
            print("else", mid, prev)
            right = mid.next
            prev.next = None
            print("else, L:", left, "R:", right)
            if left:
                root.left = get_bst(left)
            if right:
                root.right = get_bst(right)
            return root
    return get_bst(head)

if __name__ == "__main__":
    ll = LinkedList([-10,-3,0,5,9])
    t_node = TreeNode()
    print(ll)
    print(sortedListToBST(ll.head))
    
    ll = LinkedList([-10, -3, 0, 5, 9])
    print_tree(sortedListToBST(ll.head))

