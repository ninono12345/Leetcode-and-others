debug_phase = 0
debug_res = 0
print_other_than_bad = 0

class Solution:
    def get_i_of_end_of_num(self, inp):
        cnt = 0
        for c in inp:
            if c.isnumeric():
                cnt+=1
            else:
                break
        return cnt

    def find_closing_brace(self, inp):
        cnt=1
        it=0
        for c in inp:
            if c == "(":
                cnt+=1
            elif c == ")":
                cnt-=1
            if cnt==0:
                return it
            it+=1

    def calculate(self, inp):
        inp = inp.replace(" ","")

        if debug_res:
            print("gotten inp:", inp)
        res = 0
        stack = []

        i = 0

        while True:
            # if inp[i] == " ":
            #     continue

            # if inp[i]=="+" or inp[i]=="-":
            #     i+=1
            #     continue

            if debug_phase:
                print("phase 1")

            # repeat code 2
            if i == len(inp) or inp[i] == ")":
                for s in stack:
                    res+=int(s)
                if debug_res:
                    print("TEMP res1:", res)
                return res
            # end of repeat code 2

            if debug_phase:
                print("phase 1.5")

            if inp[i].isnumeric():
                num_length = self.get_i_of_end_of_num(inp[i:])
                full_num = "".join(inp[i:i+num_length])
                if i==0 or inp[i-1]=="+":
                    stack.append("+"+full_num)
                elif inp[i-1]=="-":
                    stack.append("-"+full_num)
                
                i+=num_length
                continue
            
            
            if debug_phase:
                print("phase 2")

            # repeat code 2
            if i == len(inp) or inp[i] == ")":
                for s in stack:
                    res+=int(s)
                if debug_res:
                    print("TEMP res2:", res)
                return res
            # end of repeat code 2
            
            
            if debug_phase:
                print("phase 2.5")

            if inp[i] == "*" or inp[i] == "/":
                sign_and_num = stack.pop()
                sign = sign_and_num[0]
                full_num = int("".join(sign_and_num[1:]))

                if inp[i+1].isnumeric():
                    next_num_length = self.get_i_of_end_of_num(inp[i+1:])
                    full_next_num = int(inp[i+1:i+1+next_num_length])
                    i_plus = next_num_length + 1
                elif inp[i+1]=="(":
                    # repeat code 1
                    last_brace = self.find_closing_brace(inp[i+2:])
                    full_next_num = self.calculate(inp[i+2:i+2+last_brace])
                    # end of repeat code 1
                    i_plus = last_brace + 3
                else:
                    print("* or / -> \"(\" edge case")
                    raise

                if inp[i]=="*":
                    full_num *= full_next_num
                if inp[i]=="/":
                    # full_num //= full_next_num
                    full_num = int(full_num/full_next_num)

                final_num = str(full_num)
                if final_num[0] != "-":
                    final_num = sign+final_num
                stack.append(final_num)
                i+=i_plus
                continue
            
            
            if debug_phase:
                print("phase 3")

            # repeat code 2
            if i == len(inp) or inp[i] == ")":
                for s in stack:
                    res+=int(s)
                if debug_res:
                    print("TEMP res3:", res)
                return res
            # end of repeat code 2
            
            if debug_phase:
                print("phase 3.5")

            if inp[i] == "(":
                # repeat code 1
                last_brace = self.find_closing_brace(inp[i+1:])
                braces_res = str(self.calculate(inp[i+1:i+1+last_brace]))
                # end of repeat code 1
                
                if i==0 or inp[i-1]=="+":
                    if braces_res[0]=="-":
                        stack.append("-"+braces_res[1:])
                    else:
                        stack.append("+"+braces_res)
                elif inp[i-1]=="-":
                    if braces_res[0]=="-":
                        stack.append("+"+braces_res[1:])
                    else:
                        stack.append("-"+braces_res)

                i+=last_brace+2
                continue

            i+=1

        return 0





# AI generated test set
test_dict = {
  "tier_1_sanity": [
    { "input": "3", "expected": 3 },
    { "input": "1+1", "expected": 2 },
    { "input": "10-3", "expected": 7 },
    { "input": "2*3", "expected": 6 },
    { "input": "8/2", "expected": 4 }
  ],
  "tier_2_precedence": [
    { "input": "1+2*3", "expected": 7 },
    { "input": "2*3+1", "expected": 7 },
    { "input": "10-2*3", "expected": 4 },
    { "input": "6/2*3", "expected": 9 },
    { "input": "14-3*2+5", "expected": 13 }
  ],
  "tier_3_integer_division": [
    { "input": "7/2", "expected": 3 },
    { "input": "1+7/2", "expected": 4 },
    { "input": "14/3/2", "expected": 2 },
    { "input": "2*3/4", "expected": 1 }
  ],
  "tier_4_parentheses": [
    { "input": "(1+2)", "expected": 3 },
    { "input": "(1+2)*3", "expected": 9 },
    { "input": "2*(3+4)", "expected": 14 },
    { "input": "(1+2)*(3+4)", "expected": 21 },
    { "input": "((1+2))", "expected": 3 },
    { "input": "((2+3)*4-1)/2", "expected": 9 }
  ],
  "tier_5_deep_nesting": [
    { "input": "2*(5+5*2)/3+(6/2+8)", "expected": 21 },
    { "input": "(2+6*3+5-(3*14/7+2)*5)+3", "expected": -12 },
    { "input": "1-(5-(3-2))", "expected": -3 },
    { "input": "(((((5)))))", "expected": 5 }
  ],
  "tier_6_unary_and_whitespace": [
    { "input": "-2+3", "expected": 1 },
    { "input": "3+(-2)", "expected": 1 },
    { "input": "-(3+2)", "expected": -5 },
    { "input": " 1 + 2 ", "expected": 3 },
    { "input": "1 + (  2*3 )", "expected": 7 }
  ]
}
# end of AI generated

from_tier = 0
to_tier = 6

obj = Solution()

for n, t in dict(list(test_dict.items())[from_tier:to_tier]).items():
    print("-----"+n+"-----")
    for item in t:
        if print_other_than_bad:
            print("start", item["input"], "expected:", item["expected"])
        res = obj.calculate(item["input"])
        if res != item["expected"]:
            print(item["input"], "!=", res, "expected:", item["expected"], "INCORECT!!!!!!")
        elif print_other_than_bad:
            print(item["input"], "==", res)