# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

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


def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(slow, fast)

    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    second_head = prev
    print(second_head, head)

    temp = head
    while temp and temp.next and second_head.next:
        second_next = second_head.next
        temp.next, second_head.next = second_head, temp.next
        temp = temp.next.next
        second_head = second_next
        print(head)





ll = LinkedList([1, 2, 3, 4, 5, 6, 7])
print(ll)
print("Answer:", reorderList(ll.head))

