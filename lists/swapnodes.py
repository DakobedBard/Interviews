

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapnodes(head):
    if head == None:
        return
    if head.next == None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        node1 = current.next
        node2 = current.next.next





head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)