from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        window = set()
        
        # for i in range(k):
        #     if nums[i] in window:
        #         return True
        #     window.add[nums[i]]
        
        last_i = 0
        window.add(nums[0])
        for i in range(1, n):
            if len(window)>k:
                window.remove(nums[last_i])
                last_i += 1
            
            if nums[i] in window:
                return True
            
            window.add(nums[i])
            print(window)
        
        return False
            



obj = Solution()
nums = [1,2,3,1]
nums = [1,2,3,1,2,3]
print(obj.containsNearbyDuplicate(nums, 2))