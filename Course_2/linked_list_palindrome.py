# Given a linked list's head. Return True if a list is a palindrome and False if it is not.

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
        return "".join(map(str, out))


def isPalindrome(head):
    is_palindrome = True
    frwd = str(head)
    previous = None
    node = head
    while node:
        temp = node.next
        node.next = previous
        previous = node
        node = temp
    bwd = str(previous)
    #print(frwd, bwd)
    if frwd != bwd:
        is_palindrome = False

    return is_palindrome


if __name__ == "__main__":
    node2 = Node(None, 5)
    node1 = Node(node2, 2)

    # check that your code works correctly on provided example
    assert not isPalindrome(node1), 'Wrong answer'

    node3 = Node(None, 2)
    node2 = Node(node3, 5)
    node1 = Node(node2, 2)

    # check that your code works correctly on provided example
    assert isPalindrome(node1), 'Wrong answer'