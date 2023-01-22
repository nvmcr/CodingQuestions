class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        #prefix oper
        prefix = 1
        for idx, num in enumerate(nums):
            answer[idx] = prefix # 1, 1, 2, 6
            prefix *= num       # 1, 2, 6, 24
        #postfix multily with prefix
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer
