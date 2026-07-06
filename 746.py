from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        curr_cost = [0]

        min_costs = []

        i = 0
        while True:
            if i==0:
                min_costs.append(cost[0])
                i+=1
                continue
            if i==1:
                min_costs.append(cost[1])
                i+=1
                continue

            if i==n:
                break
            # print(min_costs[i-2]+cost[i], min_costs[i-1]+cost[i])
            min_costs.append(min(min_costs[i-2], min_costs[i-1])+cost[i])
            i+=1

            # if i==n:
            #     break
        
        # print(min_costs)
        return min(min_costs[i-1], min_costs[i-2])



cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
cost = [0,1,1,1]
# cost = [1,2,2,0]
# cost = [1,2,0,0]
# cost = [1,2,3,1]
obj = Solution()
print(obj.minCostClimbingStairs(cost))