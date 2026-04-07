class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_dig = sum([(digits[i]*(10**(len(digits)-i-1))) for i in range(len(digits))])

        return [int(dig) for dig in str(sum_dig+1)]