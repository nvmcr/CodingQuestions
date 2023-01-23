class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Imagine as a linked list and use Floyds hare and tortoise to detect circle
        slow = fast = nums[0]
        #There will always be a duplicate because there are n+1 integers in [1,n] range
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: #Intersection point
                break
        slow2 = nums[0]
        while slow2 != slow: #Until they meet at the circle start(duplicate)
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow
