class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        """
        #approach:
        I guess I just prefer arithmetics when possible instead of iterations
        if no number is missing, we'll have a complete arithmetic progression, else, if 1 number is missing, we'll have a break in the series such that if that number is added, we will have the expected sum = actual sum of the numbers given + the missing number
        formula of sum in an A.P: Sn = (n/2) * (min num + max num), where n is how many numbers given
        trap:
        don't take 0 for your min_num, because the Sn formula for A.P takes the least integer is 1; even though 0 doesn't make a difference, it does when using the formula.
        use max_nums as the number of nums given. using len(nums) may give a +1 or -1 error in the value of the expected sum, as it varies due to the missing value and also the presence of 0

        #cases:
        1. return 0 if 0 not present
        2. return the difference in sums if they differ
        3. since it is established that that missing number exists, if none of 1 and 2 are true, it must be the last number then; return max_sum + 1.
        """
        if nums:
            if len(nums) < 2:
                if nums[0] == 0:
                    return 1
                else:
                    return 0
            else:
                for i in range(len(nums)-1):
                    expected_sum = int(((max(nums))/2)*(1 + max(nums)))
                    given_sum = int(sum(nums))
                    if expected_sum > given_sum:
                        return expected_sum - given_sum
                    else:
                        if 0 in nums:
                            return max(nums) + 1
                        else:
                            return 0

        return 0  