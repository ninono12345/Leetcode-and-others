from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        L = 0
        R = 0
        total = 0
        cur_best = float("inf")
        found_best = False
        
        for R in range(n):
            total += nums[R]
            while total>=target:
                found_best = True
                cur_best = min(cur_best, R-L+1)
                total-=nums[L]
                L+=1
        # print(cur_best)
        if not found_best:
            return 0
        return cur_best


target = 7
nums = [2,3,1,2,4,3]
target = 4
nums = [1,4,4]
obj = Solution()
print(obj.minSubArrayLen(target, nums))