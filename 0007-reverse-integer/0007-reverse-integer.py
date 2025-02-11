class Solution:
    def reverse(self, x: int) -> int:
        
        
        sign = 1 if x>=0 else -1
        x = abs(x)
        s = str(x)[::-1]
        result = sign * int("".join(s))
        return result if -2**31 <= result <= 2**31-1 else 0
        
