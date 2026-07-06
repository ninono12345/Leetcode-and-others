from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        sub_arrays = 0
        summ = 0
        last_i = 0
        total_i = 0
        # for i in range(n-k+1):
        #     avg = sum(arr[i:i+k])/k
        #     # print(arr[i:i+k],avg)
        #     print(sum(arr[i:i+k]), avg)
        #     if avg>=threshold:
        #         sub_arrays += 1
        # return sub_arrays
        for i in range(n):
            if total_i>=k:
                summ -= arr[last_i]
                total_i-=1
                last_i+=1
            
            summ+=arr[i]
            total_i+=1

            avg = summ/k
            print(summ, avg)
            if avg >= threshold and total_i==k:
                sub_arrays += 1
        return sub_arrays



arr = [2,2,2,2,5,5,5,8]
arr = [11,13,17,23,29,31,7,5,2,3]
obj = Solution()
print(obj.numOfSubarrays(arr, 3, 5))