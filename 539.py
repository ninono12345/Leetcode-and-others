from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times_minutes = []
        for t in timePoints:
            hours, minutes = t.split(":")
            times_minutes.append(int(hours)*60+int(minutes))
        
        times_minutes.sort()
        min_diff = float('inf')
        for i in range(len(times_minutes)):
            # diff = abs(times_minutes[i] - times_minutes[i+1])
            # if times_minutes[i]>times_minutes[i+1]:
            #     to_test = times_minutes[i]
            # else:
            #     to_test = times_minutes[i+1]
            # print("tt",to_test)
            # diff_good = min(diff, abs(to_test-1440))
            # min_diff = min(min_diff, diff_good)
            if i == len(times_minutes)-1:
                diff = abs(times_minutes[i] - times_minutes[0])
            else:
                diff = abs(times_minutes[i] - times_minutes[i+1])
            diff2 = abs(diff - 1440)
            min_diff = min(min_diff, diff, diff2)
        
        # print(min_diff)
        # print(times_minutes)
        return min_diff



obj = Solution()
times = ["00:00","23:59","00:00"]
times = ["23:59","00:00"]
times = ["12:12","00:13"]
times = ["02:39","10:26","21:43"]
print(obj.findMinDifference(times))