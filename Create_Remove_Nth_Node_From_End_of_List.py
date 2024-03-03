#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1 = head
        temp2 = head.next
        p = 0
        while(n!=p and temp1.next != None ):
            temp1 = temp1.next
            temp2 = temp2.next
            p=p+1
        
        temp3 = temp2
        temp1.next = temp3.next
        temp3 = None
        
        return head
