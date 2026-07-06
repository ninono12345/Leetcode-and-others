from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        # window = set()
        window = deque()
        
        best = 0
        L = 0
        R = 0
        for R in range(n):
            if s[R] not in window:
                window.append(s[R])
            else:
                best = max(best, len(window))
                print(best)
                while window.popleft() != s[R]:
                    continue
                window.append(s[R])
            print(window)
        return max(len(window),best)
            


s = "abcabcbb"
# s = "pwwkew"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))