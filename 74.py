from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y=len(matrix)
        x=len(matrix[0])

        Ly = 0
        Ry = y-1

        while Ly<=Ry:
            mid = (Ly+Ry) // 2
            print("mid", mid)
            
            if target>matrix[mid][-1]:
                Ly = mid+1
            
            elif target<matrix[mid][0]:
                Ry = mid-1
            
            else:
                L=0
                R=x-1
                arr = matrix[mid]
                last_mid = float("-inf")

                while L<=R:
                    midd = (L+R) // 2
                    print("midd", midd, arr[midd], "LR", L, R)

                    if target>arr[midd]:
                        print(L, midd)
                        L=midd+1
                    
                    elif target<arr[midd]:
                        R=midd-1
                    
                    else:
                        return True
                    
                    # if midd == last_mid:
                    #     print("ret extra")
                    #     return False
                    last_mid = midd
        
                return False
        return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
matrix = [[1,3,5]]
target = 1
matrix = [[1,3]]
target = 3
matrix = [[1]]
target = 2
# matrix = [[1,3,5]]
# target = 5
obj = Solution()
print(obj.searchMatrix(matrix, target))