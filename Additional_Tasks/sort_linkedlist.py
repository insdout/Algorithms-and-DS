# Given the head of a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the
# depth of the two subtrees of every node never differ by more than 1.
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


#
# TODO: ПЕРЕДЕЛАТЬ БЕЗ РЕКУРСИИ!
#

def sortList(head):
    def find_mid(start):
        slow = start
        fast = start.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(head1, head2):
        insert_point = new_head = ListNode()
        while head1 and head2:
            if head1.val > head2.val:
                insert_point.next = head2
                head2 = head2.next
            else:
                insert_point.next = head1
                head1 = head1.next
            insert_point = insert_point.next
        if head1:
            insert_point.next = head1
        if head2:
            insert_point.next = head2
        return new_head.next

    if not head or not head.next:
        return head

    left = head
    mid = find_mid(left)
    temp = mid.next
    mid.next = None
    right = temp
    print(left, right)
    l1 = sortList(left)
    l2 = sortList(right)
    return merge(l1, l2)

if __name__ == "__main__":
    ll = LinkedList([6, 7, 1, 4, 2, 5, 3])
    print(ll)
    print("Answer:", sortList(ll.head))

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