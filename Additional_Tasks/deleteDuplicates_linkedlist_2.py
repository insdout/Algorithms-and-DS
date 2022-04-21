# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list. Return the linked list sorted as well.
#
# Example 1:
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

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
    link_to_prev = None
    while node:
        print()
        print("start:", node, "prev_val", prev,"link_to_prev",link_to_prev, "head", head)
        if prev and prev.val == node.val:
            while node and prev.val == node.val:
                node = node.next

            print("node:", node, prev.val)
            if link_to_prev:
                link_to_prev.next = node
                prev = node
                print("join", link_to_prev, "prev", prev, "head", head)
            else:
                head = node
                prev = None
                link_to_prev = None
                print("move head", head)
            print("IF: prev", prev, "head", head, "link_to_prev", link_to_prev)
        else:
            link_to_prev = prev
            prev = node
            node = node.next
            print("ELSE: prev", prev, "head", head, "link_to_prev", link_to_prev)
        print("list", head)
    return head

def deleteDuplicates2(head):
    if head is None:
        return head
    if head.next is None:
        return head

    node = head
    left = right = head
    link_to_left = None
    while right:
        counter = 0
        while right and left.val == right.val:
            right = right.next
            counter += 1
        if link_to_left is None and counter > 1:
            head = left = right
        elif link_to_left is not None and counter > 1:
            link_to_left.next = right
            left = right
        else:
            link_to_left = left
            left = right
    return head


ll = LinkedList([7, 7, 1, 2, 2, 3, 3])
print(ll)
print("Answer:", deleteDuplicates2(ll.head))

ll = LinkedList([7, 7])
print(ll)
print("Answer:", deleteDuplicates2(ll.head))

ll = LinkedList([7])
print(ll)
print("Answer:", deleteDuplicates2(ll.head))
#
ll = LinkedList([1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 6, 7, 6, 6])
# print(ll)
print("Answer:", deleteDuplicates2(ll.head))