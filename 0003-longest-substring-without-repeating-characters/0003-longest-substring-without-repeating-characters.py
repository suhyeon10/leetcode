class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        num = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in num:
                num.remove(s[left])
                left+=1
            
            num.add(s[right])
            max_length = max(max_length, len(num))
        return max_length
