# Definition for singly-linked list.


class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


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
        return(str(str_repr))


ll = LinkedList([7,1,2,3])
print(ll)

def swapPairs(head):
    if not head:
        return head
    if head.next == None:
        return head

    next_pair = None
    if head.next.next:
        prev_pair_end = head
        tmp = head.next.next
        head.next, head.next.next = next_pair, head
    head = tmp

    next_pair = None
    prev_pair_end = None
    while head.next:
        tmp = head.next
        tmp_head = head
        head, head.next = next_pair, head
        head.next = prev_pair_end
        prev_pair_end = head