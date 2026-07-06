class Solution:
    gf = {}

    def fib(self, n: int) -> int:
        # if n in self.gf:
        #     return self.gf[n]
        if n<=1:
            return n
        
       
        # self.gf[n] = self.fib(n-2)+self.fib(n-1)
        # return self.gf[n]

        cn0 = 0
        cn1 = 1
        total_sum=0
        i = 2
        while True:
            total_sum=cn0+cn1
            cn0 = cn1
            cn1=total_sum
            print(cn0, cn1, total_sum)
            if i==n:
                break
            i+=1
        
        return total_sum


n=4
obj = Solution()
print(obj.fib(n))