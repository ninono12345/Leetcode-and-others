class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        f = start.replace("X", "")
        s = result.replace("X", "")
        print(f)
        print(s)
        if f != s:
            return False

        start = list(start)
        result = list(result)
        S = 0
        R = 0
        length = len(start)
        if length == 1:
            return start == result
        
        gS = False
        gR = False

        valueS = None
        valueR = None
        while True:
            if S == length or R == length:
                return True
            if not valueS:
                if start[S] == "X":
                    S += 1
                else:
                    valueS = start[S]
                    
            if not valueR:
                if result[R] == "X":
                    R += 1
                else:
                    valueR = result[R]
            
            if valueS and valueR:
                if valueS == "L":
                    if S < R:
                        return False
                elif valueS == "R":
                    if S > R:
                        return False
                
                S+=1
                R+=1
                valueS=None
                valueR=None


                



# start =  "RXXLRXRXL"
# result = "XRLXXRRLX"
start =  "LXXLXRLXXL"
result = "XLLXRXLXLX" # false
# start = "RXXLRXRXL"
# result = "XRLXXRRLX"
# start = "RXXLRXRXL"
# result = "XRLXXRRLX"
# start = "XLLR"
# result = "LXLX" # false
# start = "XXXXXLXXXX"
# result = "LXXXXXXXXX" # true

obj = Solution()
print(obj.canTransform(start, result))