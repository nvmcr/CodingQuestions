class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) -  1
        while first < last:
            twosum = numbers[first] + numbers[last]
            if twosum == target:
                return [first+1,last+1] #Result indices starting from 0
            elif twosum > target:
                last -= 1
            else:
                first += 1
