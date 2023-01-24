# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #This problem has three parts
        #First we need to find the middle and divide the list into two at mid
        #Second we will reverse the second part of the list
        #And merge both first and second

        #Finding middle using two pointers
        slow, fast = head, head.next
        while fast and fast.next: #We anyone became Null, slow is at mid
            slow = slow.next
            fast = fast.next.next
        #Partition at mid
        second = slow.next
        #Making the first list end as Null
        slow.next = None
        
        #Reversing the second list
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        #prev is at the last node of the list
        second, first = prev, head
        #Merging one from first and one from last
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
