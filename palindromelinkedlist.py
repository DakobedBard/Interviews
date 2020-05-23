class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def palindromelist(head):
    if head == None:
        return True

node = ListNode(1)
node.next = ListNode(2)
