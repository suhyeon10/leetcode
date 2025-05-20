class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        closet = float('inf')

        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1

            while(left < right):
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closet - target ):
                    closet = current_sum

                if target == current_sum:
                    return current_sum
                elif target < current_sum:
                    right-=1
                else:
                    left+=1
        return closet