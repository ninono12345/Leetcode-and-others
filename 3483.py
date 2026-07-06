from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        digits = [str(d) for d in digits]
        set_of_combinations = set()
        for i in range(n):
            for j in range(n):
                if i==j or digits[i]=="0":
                    continue
                for k in range(n):
                    if i==k or j==k:
                        continue
                    # set_of_combinations.add(int("".join(list(set(digits[i]+digits[j]+digits[k])))))
                    # print(digits[i]+digits[j]+digits[k])
                    set_of_combinations.add(int((digits[i]+digits[j]+digits[k])))
        
        # print(set_of_combinations)
        return len([s for s in set_of_combinations if s%2==0 and s>=100])


digits = [1,2,3,4]
# digits = [0,2,2]
obj = Solution()
print(obj.totalNumbers(digits))

# print(str(list("labas")))