"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            x = nums[i]
            nums.remove(x)
            if x in nums:
                return True

        return False
passed 13/21
"""

"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = [nums.count(x) for x in nums if nums.count(x) > 1]
        return (not len(newList) == 0)

passed all
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = set(nums)
        return (not len(nums) == len(new_nums))