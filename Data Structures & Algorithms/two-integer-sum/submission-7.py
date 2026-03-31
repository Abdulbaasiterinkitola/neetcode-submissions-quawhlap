class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                return [i, (nums.index(diff, i+1))]
                
"""
        indexMap = {}

        for i, x in enumerate(nums):
            diff = target - x
            if diff in indexMap:
                return [indexMap[diff], i]
            indexMap[x] = i
correct
"""