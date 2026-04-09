class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #instead of the long solution earlier, this works w/o overthinking:
        n = len(nums)
        
        # sum of sequence from 0 to n: (n * (n + 1)) / 2
        expected_sum = n * (n + 1) // 2
        
        # the difference is exactly the missing number
        return expected_sum - sum(nums)