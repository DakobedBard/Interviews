


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeAtPosition(head, data, position):

    if position ==0:
        newhead = ListNode(data)
        newhead.next = head
        return newhead
    dummy = ListNode(-1)
    dummy.next = head
    current = head
    n = 0

    while(n<position):
        dummy = dummy.next
        current = current.next
        n+=1;
    dummy.next = ListNode(data)
    dummy.next.next = current
    return head

def printlist(head):
    current = head
    while(current):
        print(current.data)
        current = current.next

# head = ListNode(3)
head = ListNode(16)
head.next = ListNode(13)
head.next.next = ListNode(7)

newlist = insertNodeAtPosition(head, 1,0)
printlist(newlist)
# head.next.next.next = ListNode(1)