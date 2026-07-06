from typing import List
from collections import deque

# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         max_sum = float("-inf")
#         cur_sum = 0
#         n = len(nums)
#         last_i = 0
#         # for n in nums:
#         #     cur_sum = max(cur_sum+n, n)
#         #     max_sum = max(cur_sum, max_sum)
#         # if max_sum < 0:
#         #     return max_sum
        
#         # total_sum = sum(nums)
#         # cur_sum = 0
#         # min_sum = float("inf")
#         # for n in nums:
#         #     cur_sum = min(cur_sum+n, n)
#         #     min_sum = min(cur_sum, min_sum)
#         # if min_sum == total_sum:
#         #     return max_sum
        
#         # return max(max_sum, total_sum - min_sum)
#         # for i in range(0, n*2):
            

#         #     if i-last_i == n:
#         #         cur_sum-=nums[last_i%n]
#         #         last_i+=1
#         #         while nums[last_i%n] < 0:
#         #             cur_sum-=nums[last_i%n]
#         #             last_i+=1

#         #     print(max_sum)
#         #     max_sum = max(max_sum, cur_sum)

#         #     if cur_sum<0:
#         #         cur_sum = 0
#         #         last_i = i

#         #     cur_sum+=nums[(i)%n]

#         #     print("n", i, last_i, nums[(i)%n])
#         #     if i<n:
#         #         print("s1",cur_sum, nums[last_i%n:i%n+1])
#         #     else:
#         #         print("s2",cur_sum, nums[last_i%n:]+nums[:i%n+1])

        
#         # return max_sum

#         prefix_sums = [0] * (n * 2+1)
#         for i in range(n * 2):
#             prefix_sums[i+1] = prefix_sums[i] + nums[i%n]
#             print(prefix_sums[i+1])
#         print(prefix_sums)

#         dq = deque()

#         for i in range(n * 2):
#             if i - dq[0] == n:
#                 cur_sum-=nums
#                 dq.popleft()
            
#             cur_sum = 

#         # for i in range(0, n*2):
#         #     if S>=E:
#         #         sm = sum(nums[S:])+sum(nums[:E])
#         #         print("s1",nums[S:]+nums[:E], S, E)
#         #         if S==E:
#         #             S+=1
#         #             if S==n:
#         #                 S = 0
#         #             while nums[S]<0:
#         #                 S+=1
#         #                 if S==n:
#         #                     S = 0
#         #                 print("n", nums[S])
#         #     else:
#         #         sm = sum(nums[S:E])
#         #         print("s2", nums[S:E], S, E)
#         #     if sm < 0:
#         #         print("less 0")
#         #         S = E
#         #     E+=1
#         #     if E==n:
#         #         E = 0
#         #     print(sm)
#         #     max_sum = max(max_sum, sm)
#         #     # print(max_sum)
#         # return max_sum
#         #     print("i", i%n, "last_i", last_i, "n",nums[(i)%n])
#         #     # print("n",nums[(i)%n])
#         #     # cur_sum = max(cur_sum, 0)
#         #     if i%n == last_i:
#         #         break
#         #     if cur_sum<0:
#         #         cur_sum = 0
#         #         last_i = i
#         #     cur_sum+=nums[(i)%n]
#         #     max_sum = max(max_sum, cur_sum)
#         #     # print("cs",cur_sum)
#         # # print()
#         # return max_sum
#         # end_it = 0
#         # max_cnt = 0
#         # while True:
#         #     if end_it != n nums[end_it] >= 0 or :
#         #         end_it+=1
#         #         max_cnt += 1
#         #     else:
#         #         nums = nums[end_it:]+nums[:end_it]
#         #         print(nums)
#         #         for n in nums:
#         #             cur_sum = max(cur_sum+n, n)
#         #             max_sum = max(cur_sum, max_sum)
#         #             while nums[end_it] < 0:
#         #                 end_it += 1
#         #         if max_cnt == n:
#         #             return max_sum
        
        
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_array = [0 for i in range(n*2+1)]
        for i in range(n*2):
            prefix_array[i+1] = prefix_array[i]+nums[i%n]
        print(prefix_array)

        max_num = float("-inf")
        dq = deque()
        dq.append(0)
        
        for i in range(1,n*2):
            print("dq", dq[-1], dq[0], dq[-1]-dq[0])
            # if dq[-1]-dq[0] >= n:
            if i-dq[0] > n:
                dq.popleft()
                print("dq2",dq)
            
            calc = prefix_array[i] - prefix_array[dq[0]]
            max_num = max(calc, max_num)
            while len(dq) != 0 and prefix_array[i] <= prefix_array[dq[-1]]:
                dq.pop()
                print("dq1",dq)
            
            # if is_true:
            dq.append(i)
            
            # if prefix_array[i] >= prefix_array[dq[-1]]:
            #     dq.append(i)
            # else:
            #     dq.pop()
            #     dq.append(i)
            print("---")
            print(prefix_array[i])
            print(max_num)
            print(dq)
        return max_num


obj = Solution()
nums = [5,-3,5]
# nums = [1, -2, 3, -2]
# nums = [3,1,3,2,6]
# nums = [-3,-2,-3]
# nums = [-2]
# nums = [9,4,-5,4,5,-9,4]
# nums = [6,9,-3]
# nums = [-2, 4, -1, 4, -1]
print(obj.maxSubarraySumCircular(nums))