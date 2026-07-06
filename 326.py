class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n==1 or n==3:
        #     return True
        # if n<1:
        #     return False
        
        # return self.isPowerOfThree(n/3)

        if n<=0:
            return False
        
        max_i=0
        max_val = 2**31-1
        max_3_val = 0
        print(max_val)
        for i in range(32):
            if 3**i<max_val:
                print(3**i)
                print(i)
                max_i = i
                max_3_val = 3**i
            else:
                break
        
        if max_3_val%n == 0:
            return True
        else:
            return False
            



n = 30
obj = Solution()
print(obj.isPowerOfThree(n))