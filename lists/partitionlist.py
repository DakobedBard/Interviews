class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printlist(head):
    while head:
        print(head.val)
        head = head.next


def partition(head, x):
    before_head = ListNode(None)
    before = before_head
    after_head = ListNode(None)
    after = after_head

    while(head != None):
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    after.next = None
    before.next = after_head.next
    return before_head.next
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
x = 3
newlist = partition(head, 3)
printlist(newlist)