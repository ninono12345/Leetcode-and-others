from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        # fix = [False]*n
        current_best = 1
        if n == 1:
            return 1
        if n == 2:
            if arr[0] == arr[1]:
                return 1
            return 2
        
        current_best = 1
        if arr[1] != arr[0]:
            current_best+=1
        
        best_unbroken_chain = 0
        if arr[1] > arr[0]:
            prev = True
            unbroken_chain = 2
        elif arr[1] < arr[0]:
            prev = False
            unbroken_chain = 2
        else:
            prev = None
            unbroken_chain = 1
        for i in range(2, n):
            if prev is None:
                if arr[i] > arr[i-1]:
                    prev = True
                    unbroken_chain = 2
                elif arr[i] < arr[i-1]:
                    prev = False
                    unbroken_chain = 2
                else:
                    prev = None
                    unbroken_chain = 1
                best_unbroken_chain = max(best_unbroken_chain, unbroken_chain)
                continue

            if arr[i] > arr[i-1]:
                if prev:
                    unbroken_chain = 2
                    prev = True
                else:
                    unbroken_chain +=1
                    prev = True
            elif arr[i] < arr[i-1]:
                if prev:
                    unbroken_chain += 1
                    prev = False
                else:
                    unbroken_chain = 2
                    prev = False
            else:
                prev = None
                unbroken_chain = 1
            
            best_unbroken_chain = max(best_unbroken_chain, unbroken_chain)
        
        return best_unbroken_chain

        # n = len(arr)
        # if n == 1:
        #     return 1
        # if n == 2:
        #     if arr[0] == arr[1]:
        #         return 1
        #     return 2
        
        # B = 0
        # E = 1

        # diff = [0]*n
        # for i in range(1, n):
        #     diff[i]=arr[i]-arr[i-1]
        #     # print()
        # print(diff)
                
        

obj = Solution()
arr = [9,4,2,10,7,8,8,1,9]
# arr = [100,100,100]
print(obj.maxTurbulenceSize(arr))