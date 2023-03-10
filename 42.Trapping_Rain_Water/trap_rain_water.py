class Solution:
    def trap(self, height: List[int]) -> int:
        #Only trick is Water_Stored_atindex = min(Max_of_Left_of_index, Max_of_Right_of_Index) - height[index]
        # We can have array maintaining max_left_of_index and another array for max_right
        #Or do two pointers
        l, r = 0, len(height)-1
        max_l, max_r = height[0], height[-1]
        storage = 0
        while l < r:
            if max_l < max_r: #(min(Max_of_Left_of_index, Max_of_Right_of_Index))
                l += 1
                max_l = max(max_l,height[l])
                storage += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                storage += max_r - height[r]
        return storage
