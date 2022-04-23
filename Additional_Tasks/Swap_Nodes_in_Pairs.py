# Definition for singly-linked list.
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


def swapPairs(head):
    if not head:
        return head
    if not head.next:
        return head


    prev_node = None
    cur_node = head

    while cur_node and cur_node.next:
        print("============")
        print("start:", cur_node)
        tmp = cur_node
        tmp2 = cur_node.next
        print(id(tmp), id(cur_node), tmp == cur_node, tmp is cur_node) #    <- 140539211660784 140539211660784 True True
        tmp.next, tmp2.next = tmp2.next, tmp #                              <-  Работает
        #cur_node.next, cur_node.next.next = cur_node.next.next, cur_node  # <-  Не работает
        print("tmp", tmp,"tmp2", tmp2)
        cur_node = tmp2
        print("cur_node", cur_node)
        if prev_node:
            prev_node.next = cur_node
        else:
            head = cur_node
        prev_node = cur_node.next
        cur_node = cur_node.next.next
    return head

ll = LinkedList([7, 1, 2, 3])
print(ll)
print("sw:", swapPairs(ll.head))