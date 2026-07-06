class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        to_add = []
        while True:
            ta = ""
            for c in word:
                # print(c)
                ta +=chr(ord(c)+1)
            word+=ta
            # print(word)
            if len(word) > k:
                break
        # print(word)
        return word[k-1]


k = 5
obj = Solution()
print(obj.kthCharacter(k))

# print(chr(ord('c') + 1))