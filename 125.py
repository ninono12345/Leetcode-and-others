class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([l for l in s if l.isalnum()])
        print(s)

        L = 0
        R = len(s)-1

        while L<R:
            if s[L]==s[R]:
                print(s[L], s[R])
                L+=1
                R-=1
            else:
                print(s[L], s[R])
                return False
        
        return True


s = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(s))