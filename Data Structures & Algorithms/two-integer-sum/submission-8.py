class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       """ for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                return [i, (nums.index(diff, i+1))]
       #this is O(N2)         
       """

       index_map = {}

       for index, val in enumerate(nums):
            diff = target - val
            if diff in index_map:
                return [index_map[diff], index]
            index_map[val] = index
        














"""
        indexMap = {}

        for i, x in enumerate(nums):
            diff = target - x
            if diff in indexMap:
                return [indexMap[diff], i]
            indexMap[x] = i
correct
"""