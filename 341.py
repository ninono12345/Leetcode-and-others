# Implemented as minimal work and zero copy when looking up hasNext

class NestedIterator:
    # def __init__(self, nestedList: [NestedInteger]):
    def __init__(self, nestedList):
        self.nl = nestedList
        self.cur_nl = [[nestedList, 0]]
        # self.reach_nearest_int_or_end()
        # self.cur_nl = [nestedList]
        # self.nested_it = [0]

    # def reach_nearest_int_or_end(self):
    #     while isinstance(self.cur_nl[-1][0][self.cur_nl[-1][1]], list):
    #         print([[len(l[0]), l[1]] for l in self.cur_nl])
    #         # print("yes2", len(self.cur_nl))

    #         self.cur_nl.append([self.cur_nl[-1][0][self.cur_nl[-1][1]], 0])
    #         self.cur_nl[-2][1]+=1
    #         print("yes3")

    #         while len(self.cur_nl[-1][0]) <= self.cur_nl[-1][1]:
    #             print("yes")
    #             self.cur_nl.pop()
    #             if len(self.cur_nl)==0:
    #                 return None

    def reach_nearest_int_or_end(self):
        while True:

            if len(self.cur_nl[-1][0]) <= self.cur_nl[-1][1]:
                self.cur_nl.pop()
                if len(self.cur_nl) == 0:
                    return 1
                continue

            if isinstance(self.cur_nl[-1][0][self.cur_nl[-1][1]], list):
                self.cur_nl.append([self.cur_nl[-1][0][self.cur_nl[-1][1]], 0])
                self.cur_nl[-2][1]+=1
                continue

            if isinstance(self.cur_nl[-1][0][self.cur_nl[-1][1]], int):
                return 0


    
    # def go_up(self):

    
    def next(self) -> int:
        # print("next start")
        # if len(self.cur_nl)==0:
        #     return None
        
        # while len(self.cur_nl[-1]) <= self.nested_it[-1]:
            # self.cur_nl.pop()
            # self.nested_it.pop()

        # print(self.cur_nl)
        # print(len(self.cur_nl[-1][0]))
        # print(self.cur_nl[-1][1])
        # while len(self.cur_nl[-1][0]) <= self.cur_nl[-1][1]:
        #     self.cur_nl.pop()
        #     if len(self.cur_nl)==0:
        #         return None
            
        # while isinstance(self.cur_nl[-1][0][self.cur_nl[-1][1]], list) and len(self.cur_nl[-1][0]) == 0:
        #     self.cur_nl[-1][1]+=1

        # while isinstance(self.cur_nl[-1][self.nested_it[-1]], list):
        #     self.cur_nl.append(self.cur_nl[-1][self.nested_it[-1]])
        #     self.nested_it[-1]+=1
        #     self.nested_it.append(0)
        
        # while isinstance(self.cur_nl[-1][0][self.cur_nl[-1][1]], list):
        #     if len(self.cur_nl[-1][0][self.cur_nl[-1][1]]) == 0:
        #         self.cur_nl[-1][1]+=1
        #         continue
        #     self.cur_nl.append([self.cur_nl[-1][0][self.cur_nl[-1][1]], 0])
        #     self.cur_nl[-2][1]+=1

        end_of_list = self.reach_nearest_int_or_end()
        if end_of_list:
            return None

        elem = self.cur_nl[-1][0][self.cur_nl[-1][1]]
        self.cur_nl[-1][1]+=1

        return elem
    
        # elem = self.cur_nl[-1][self.nested_it[-1]]
        # if isinstance(elem, int):
        #     self.nested_it[-1] += 1
        #     return elem
        
        # if isinstance(elem, int):
        #     self.cur_nl[-1][1]+=1
        #     return elem
        

    def hasNext(self) -> bool:
        # stack_level = len(self.cur_nl[-1])-1
        # # curr_list = self.cur_nl[-1][0]
        # shallow_copy = [frame[:] for frame in self.cur_nl]
        # curr_it = self.cur_nl[-1][1]
        # while True:
        #     curr_list = shallow_copy[-1][0]
        #     curr_it = shallow_copy[-1][0]
        #     if len(curr_list)<=curr_it:
                
            
        #     if isinstance(curr_list[curr_it], int):
        #         return True
            
        #     while isinstance(curr_list[curr_it], list):
        def recursive(l, it):
            # print("rec")
            while True:
                if len(l)<=it:
                    return False
                
                if isinstance(l[it], int):
                    return True
                
                if isinstance(l[it], list):
                    if recursive(l[it], 0):
                        return True
                    else:
                        it+=1
                        continue
        
        for frame in reversed(self.cur_nl):
            
            if recursive(frame[0], frame[1]):
                return True
        
        return False






# Your NestedIterator object will be instantiated and called as such:

nestedList = [[1,1],2,[1,1]]
nestedList = [1,[4,[6]]]
nestedList = [[[], [[]]], [], 1, [[]], 2, 1,[4,[6, [], 7], 6], 9]

i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)
# while True:
#     n = i.next()
#     if n is None:
#         break
#     print(n)