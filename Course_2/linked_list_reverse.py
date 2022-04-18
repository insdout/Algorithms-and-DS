# Given a linked list's head, reverse it and return the head of the reversed list.

class Node:
    def __init__(self, link=None, val=None):
        self.val = val
        self.next = link
    def __repr__(self):
        out = [self.val]
        node = self.next
        while node:
            out.append(node.val)
            node = node.next
        return str(out)
    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

def reverseLL(head):
    reversed_head = Node()
    if not head or not head.next:
        return head
    previous = None
    while head:
        temp = head.next
        head.next = previous
        previous = head
        head = temp
    reversed_head.next = previous.next
    reversed_head.val = previous.val
    return reversed_head

if __name__ == "__main__":
    node2 = Node(None, 5)
    node1 = Node(node2, 2)

    # check that your code works correctly on provided example
    print(reverseLL(node1) == Node(node1, 5))
    assert reverseLL(node1) == Node(node1, 5), 'Wrong answer'