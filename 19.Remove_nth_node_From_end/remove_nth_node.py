# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Create a dummy linked list and append at the beginning
        dummy = ListNode(0,head)
        #Initializing two pointers and these two are seperated by a distance of n + 1.
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right: #If right reaches null then left.next is the node to be removed
            left = left.next
            right = right.next
        left.next = left.next.next #skipping is nothing but deleting
        return dummy.next
