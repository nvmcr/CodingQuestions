# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node, next_node = None, None
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        head = curr_node
        return prev_node
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head #Empty.
        if not head.next: return head #We reached end.
        orig_head = self.reverseList(head.next) #Traverse to end, orig_head is now end node.
        head.next.next = head #Swap head with right node.
        head.next = None #So we don't wind up in infinite loop.
        return orig_head #Very last thing returned. End node!
'''
