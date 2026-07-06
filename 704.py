from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L = 0
        R = n

        last_mid = float("-inf")
        while L<=R:
            mid = (L+R)//2
            print(mid)
            if nums[mid]>target:
                R=mid
            elif nums[mid]<target:
                L=mid
            else:
                return mid
            
            if mid == last_mid:
                return -1
            last_mid = mid
        return -1

nums = [-1,0,3,5,9,12]
target = 9
nums = [-1,0,3,5,9,12]
target = 2
nums = [1]
target = 2
obj = Solution()
print(obj.search(nums, target))