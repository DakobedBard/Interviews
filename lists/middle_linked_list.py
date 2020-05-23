class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    dummy = ListNode(-1)
    dummy.next = head

    slow = dummy
    fast = dummy
    while fast.next and  fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow.next.val
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

print("the middle value of this list is {}".format(middleNode(head)))