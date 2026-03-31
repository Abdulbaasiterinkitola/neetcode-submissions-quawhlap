class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(char for char in s if char.isalnum()).lower()
        reversed_s = new_s[::-1]
        
        return new_s == reversed_s 