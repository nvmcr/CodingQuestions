# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #initailize two pointers that start at head
        slow, fast = head, head
        #Iterate if fast and fast.next exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #If the fast pointer  meets slow pointer, then there is a circle
            if fast == slow:
                return True
        return False
