# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # The idea is to merge two lists at a time thus getting a O(logk) instead of O(k)

        if not lists:
            return None
        
        while len(lists) > 1:
            mergedlists = []
            for i in range(0, len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedlists.append(self.mergefunc(l1, l2))
            lists = mergedlists
        return lists[0]
    
    def mergefunc(self, l1, l2):
        res = dummy = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1 or l2:
            dummy.next = l1 if l1 else l2
        
        return res.next
