class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printlist(node):
    while node:
        print(node.val)
        node = node.next
def reverseList(head):

    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def isPalindrome(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    slow = reverseList(slow)

    fast = head

    while slow != None:
        if slow.val != fast.val:
             return False
        slow = slow.next
        fast = fast.next
    return True




head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print("This lsit is a palindrome {}".format(isPalindrome(head)))



# printlist(rev)
