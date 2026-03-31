class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for i, x in enumerate(nums):
            diff = target - x
            if diff in indexMap:
                return [indexMap[diff], i]
            indexMap[x] = i