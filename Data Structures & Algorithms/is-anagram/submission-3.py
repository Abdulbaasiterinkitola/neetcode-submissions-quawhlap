class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = [0]*26, [0]*26
        for s_char in s:
            s_char_diff = ord(s_char) - ord("a")
            s_map[s_char_diff] += 1

        for t_char in t:
            t_char_diff = ord(t_char) - ord("a")
            t_map[t_char_diff] += 1

        return s_map == t_map