class Solution:
    def myAtoi(self, s: str) -> int:

       
        s= s.lstrip()
        if len(s) <=0:
            return 0
        sign = 1
        index = 0
        result = ""
        if s[index] in ["-","+"]:
            if s[index] == "-":
                sign = -1
            index+=1

        while index<len(s) and s[index].isdigit():
            result+=s[index]
            index+=1
        
        if not result:  # 숫자가 하나도 없으면 0 반환
            return 0
            
        result = int(result)*sign
        if result > 2**31-1:
            return 2**31-1
        if result < -2**31:
            return -2**31
        
        return result

        