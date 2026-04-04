class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid_index = (l+r)//2
            if target == nums[mid_index]:
                return mid_index

            if target > nums[mid_index]:
                l = mid_index + 1
            
            elif target < nums[mid_index]:
                r = mid_index - 1
        
        return -1
        
        
        """
        l, r = 0, len(nums) - 1
        mid_index = int((l+r+1)/2)

        if nums[l] <= target <= nums[r]:
            while target != nums[mid_index] and nums[l] <= target <= nums[r]:
                if target > nums[mid_index]:
                    l = mid_index + 1
                    if nums[l] <= target <= nums[r]:
                        mid_index = int((l+r+1)/2)
                if target < nums[mid_index]:
                    r = mid_index - 1
                    if nums[l] <= target <= nums[r]:
                        mid_index = int((l+r+1)/2)

        if target == nums[mid_index]:
            return mid_index

        return -1
        # correct, but can be simplified
        """

        """
        while target > nums[mid_index] and target <= nums[r-1]:
            l = mid_index + 1
            mid_index = int((l+r)/2)

        while target < nums[mid_index] and target >= nums[l]:
            r = mid_index - 1
            mid_index = int((l+r)/2)

        if target == nums[mid_index]:
            return mid_index

        return -1
        # not correct for some test cases
        """

        """
        if target in nums:
            return nums.index(target)
        return -1
        # O(n). not efficient since we can get o(logn) with binary search
        """