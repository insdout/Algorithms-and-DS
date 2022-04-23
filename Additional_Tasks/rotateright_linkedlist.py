# Given the head of a linked list, rotate the list to the right by k places.
#
# Example 1:
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

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


def rotateRight( head, k: int) :
    from collections import deque
    if not head or not head.next:
        return head

    q = deque()
    n_head = head
    len_l = 0
    while n_head:
        len_l += 1
        n_head = n_head.next

    real_k = k % len_l

    if real_k == 0:
        return head
    n_head = head
    while n_head:
        q.append(n_head)
        while len(q) > real_k:
            q.popleft()
        n_head = n_head.next
    i = len_l - len(q)
    n_head = q.popleft()
    n_last = n_head
    #print("n_last", n_last)
    while n_last.next:
        n_last = n_last.next
    #print("n_last", n_last)
    while i and n_last:
        n_last.next = head
        n_last = n_last.next
        head = head.next
        i -= 1
    n_last.next = None
    #print(head, n_head)
    #print(real_k, len_l, last, q)
    return(n_head)


def rotateRight2( head, k: int) :
    if not head or not head.next:
        return head

    node = head
    len_list = 1
    while node.next:
        node = node.next
        len_list += 1

    k_real = k % len_list
    shift = len_list - k_real
    #print("shift:",shift, "len:",len_list,"k", k_real)
    last_node = node
    temp = head
    last_node.next = head
    prev = None
    for _ in range(shift):
        prev = temp
        temp = temp.next
        #print("temp", temp.val)
    prev.next = None
    new_head = temp
    return(new_head)

ll = LinkedList([1,2,3,4,5])
print(ll)
print("Answer1:", rotateRight(ll.head, 12))

ll = LinkedList([1,2,3,4,5])
print(ll)
print("Answer2:", rotateRight2(ll.head, 12))
