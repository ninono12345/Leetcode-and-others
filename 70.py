class Solution:
    gf = {}
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        self.gf[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.gf[n]


n = 4
obj = Solution()
print(obj.climbStairs(n))