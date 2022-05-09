class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
    def __repr__(self):
        l = [self.val]
        node = self.next
        stop = 50
        while node and stop > 0:
            l.append(node.val)
            node = node.next
            stop -= 1
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
        stop = 50
        while node and stop > 0:
            str_repr.append(node.val)
            node = node.next
            stop -= 1
        return str(str_repr)

def mergeTwoLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    head = first = list1
    second = list2
    f_prev = None
    while first and second:
        if first.val < second.val:
            f_prev = first
            first = first.next
        else:
            first_next = first
            second_head = second.next
            if f_prev:
                f_prev.next = second
            else:
                head = second
            second.next = first_next
            f_prev = second
            second = second_head
            first = first_next
    if second and f_prev:
        f_prev.next = second
    return head

l1 = LinkedList([1,2,4])
l2 = LinkedList([1,3,4])
print(mergeTwoLists(l1.head, l2.head))

l1 = LinkedList([1,2,4])
l2 = LinkedList([1,3,4,5,6])
print(mergeTwoLists(l1.head, l2.head))

l1 = LinkedList([1,2,4,5,6])
l2 = LinkedList([1,3,4])
print(mergeTwoLists(l1.head, l2.head))