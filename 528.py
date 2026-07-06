import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.picker = [0]
        for i in range(len(self.w)):
            # to_add = 0
            # for ii in range(i+1):
            #     to_add += self.w[ii]
            # self.picker.append(self.w[])
            if i == 0:
                self.picker.append(self.w[i])
            else:
                self.picker.append(self.w[i]+self.picker[-1])

    def pickIndex(self) -> int:
        rand = random.randint(1, self.picker[-1])
        print("r",rand)
        gotten_iter = -1
        max_iter = len(self.picker)
        min_iter = 0
        while True:
            new_iter = min_iter+(max_iter-min_iter)//2
            # print(new_iter)
            if rand <= self.picker[new_iter]:
                print(rand, self.picker[new_iter])
                if rand > self.picker[new_iter-1]:
                    return new_iter - 1
                max_iter = new_iter
            else:
                min_iter = new_iter
        return rand

# Your Solution object will be instantiated and called as such:
w = [1, 3, 1, 5]
obj = Solution(w)
print(obj.picker)
print(obj.pickIndex())
# param_1 = obj.pickIndex()

