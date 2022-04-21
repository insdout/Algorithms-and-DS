# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
#
# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

class ListNode:
    def __init__(self, val, next_node=None):
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

def deleteDuplicates(head):
    node = head
    prev = None
    while node:
        if prev and prev.val == node.val:
            prev.next = node.next
            node = node.next
            print("if", head)
        else:
            prev = node
            node = node.next
            print("else", head)
        print("list", head)
    return head


ll = LinkedList([7, 7, 1, 2, 2, 3, 3])
print(ll)
print("Answer:", deleteDuplicates(ll.head))

ll = LinkedList([7, 7])
print(ll)
print("Answer:", deleteDuplicates(ll.head))

ll = LinkedList([7])
print(ll)
print("Answer:", deleteDuplicates(ll.head))