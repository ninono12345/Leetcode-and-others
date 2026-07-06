from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        L = 0
        R = n-1

        while True:
            if numbers[L] + numbers[R]>target:
                R-=1
            elif numbers[L] + numbers[R]<target:
                L+=1
            else:
                return [L+1, R+1]


numbers = [2,7,11,15]
target = 9
obj = Solution()
print(obj.twoSum(numbers, target))