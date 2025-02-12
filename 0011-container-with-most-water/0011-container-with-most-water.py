class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_sum =0
        
        while left<right:
            area =  (right-left)* min(height[left], height[right]) 
            max_sum = max(area, max_sum)

            if height[left] > height[right]:
                right -=1
            else:
                left+=1
            
        
        return max_sum


        

        