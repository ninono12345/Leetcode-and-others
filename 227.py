class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        print(s)
        # while True:
        #     it1 = s.find("*")
        #     it2 = s.find("/")
        #     if it1==-1:
        #         it = it2
        #     if it2==-1:
        #         it=it1
        #     if it
        #     it = min(it1, it2)
        #     it1 = it
        #     it2 = it
        #     int1 = ""
        #     while True:
        #         it1-=1
        #         if s[it1].isdigit():
        #             int1=s[it1]+int1
        #         else:
        #             break
            
        #     int2 = ""
        #     while True:
        #         it2+=1
        #         if s[it2].isdigit():
        #             int2+=s[it2]
        #         else:
        #             break
            
        #     if s[it]=="+":
        #         ans = int(int1)+int(int2)
        #     if s[it]=="-":
        #         ans = int(int1)-int(int2)
        #     if s[it]=="*":
        #         ans = int(int1)*int(int2)
        #     if s[it]=="/":
        #         ans = int(int1)//int(int2)
            
        #     s=s[:it1+1]+str(ans)+s[it2:]
        #     print(int1, int2)
        #     print(s)
        #     break

        stack = []
        cur_num = ""
        for c in s:
            if c.isdigit():
                cur_num+=c
            else:
                stack.append(cur_num)
                cur_num=""
                cur_num+=c
        stack.append(cur_num)
        
        print("s1",stack)
        stack2 = []
        for i in range(len(stack)):
            if stack[i][0]=="*":
                ans = int(stack2[-1])*int(stack[i][1:])
                stack2[-1] = ans
            if stack[i][0]=="/":
                ans = int(int(stack2[-1])/int(stack[i][1:]))
                print(ans, stack2[-1], stack[i][1])
                stack2[-1] = ans
            if stack[i][0]!="*" and stack[i][0]!="/":
                stack2.append(int(stack[i]))
            print(stack2)
        print(stack2)

        ans = sum(stack2)
        return ans

        



s = "1+2*5/3+6/4*2"
s = " 3+5 / 2 "
s = "14-3/2"
s = "1*2-3/4+5*6-7*8+9/10"

obj = Solution()
ans = obj.calculate(s)
print(ans)