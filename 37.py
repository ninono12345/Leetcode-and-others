import copy
import bisect

class Solution:

    def get_cell_possibilities(self, i, j):
        return {"1","2","3","4","5","6","7","8","9"} - (self.occupations_3x3[i//3][j//3] | 
                                                        self.occupations_h[i] | 
                                                        self.occupations_v[j] | 
                                                        self.impossibles[i][j])
    
    def sort_possibilities(self):
        def updated_sort(x):
            x[2]=self.get_cell_possibilities(x[0], x[1])
            return len(x[2])
        self.sorted_possibilities = sorted(self.sorted_possibilities, key=updated_sort, reverse=True)
        # while len(self.sort_possibilities)
        # for sp in self.sorted_possibilities:
        #     print(len(sp[2]), sp)
        # return self.sorted_possibilities[-1]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # self.initial_board = copy.deepcopy(board)

        occupations_3x3 = [[set() for _ in range(3)] for _ in range(3)]
        occupations_h = [set() for _ in range(9)]
        occupations_v = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    occupations_3x3[i//3][j//3].add(board[i][j])
                if board[i][j]!=".":
                    occupations_h[i].add(board[i][j])
                if board[i][j]!=".":
                    occupations_v[j].add(board[i][j])

        

        self.occupations_3x3 = occupations_3x3
        self.occupations_h = occupations_h
        self.occupations_v = occupations_v

        self.impossibles = [[set() for _ in range(9)] for _ in range(9)]

        self.sorted_possibilities = []
        # initial list
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    self.sorted_possibilities.append([i, j, set()])
        
        self.sort_possibilities()

        self.tries_stack = []

        total_rollbacks = 0

        while True:
            # print("tot while")
            if len(self.sorted_possibilities) == 0:
                break
            self.sort_possibilities()
            possibility = self.sorted_possibilities.pop()
            i, j = possibility[0], possibility[1]
            
            test_number = next(iter(possibility[2]), None)
            if test_number is not None:
                board[i][j] = test_number
                forced = False
                if len(possibility[2]) == 1:
                    forced = True

                self.occupations_3x3[i//3][j//3].add(test_number)
                self.occupations_h[i].add(test_number)
                self.occupations_v[j].add(test_number)

                self.tries_stack.append((i, j, test_number, forced))
                # print("add i:", i, "j:", j, "possibilities:", possibility[2])
            
            else:
                total_rollbacks+=1
                self.sorted_possibilities.append(possibility)
                it = -1
                # print(len(self.tries_stack), "bad", i, j, "//3", i//3, j//3)
                while self.tries_stack[it][3]:
                # while self.tries_stack[it][3] or not (self.tries_stack[it][0] == i or self.tries_stack[it][1] == j or (self.tries_stack[it][0]//3 == i//3 and self.tries_stack[it][1]//3 == j//3)):
                    it-=1
                    if len(self.tries_stack) == (-it)-1:
                        for ts in self.tries_stack:
                            print(ts)
                        raise
                
                # print(self.occupations_3x3)
                # print(self.occupations_h)
                # print(self.occupations_v)
                for k in range(-1, it-1, -1):
                    last = self.tries_stack.pop()
                    # print("removing last. i:", last[0], "j:", last[1], "num:", last[2])
                    self.occupations_3x3[last[0]//3][last[1]//3].remove(last[2])
                    self.occupations_h[last[0]].remove(last[2])
                    self.occupations_v[last[1]].remove(last[2])
                    self.sorted_possibilities.append([last[0], last[1], set()])
                    
                    if k != it and len(self.impossibles[last[0]][last[1]])!=0:
                        self.impossibles[last[0]][last[1]] = set()
                        # print("reset impossible", k)
                    if k == it:
                        self.impossibles[last[0]][last[1]].add(last[2])
                        # print("add impossible", k)
                
                # print("-------")
                # possible_bad_cases = []
                # for ts in self.tries_stack:
        # print("total_rollbacks", total_rollbacks)
                



        # for i in range(9):
        #     for j in range(9):


        # print(occupations_h[0])
        # print(occupations_v[0])
        # for i in range(9):
        #     print(occupations_h)
        #     print(occupations_v)
        #     print("---")

        # possible_solutions = [[{} for _ in range(9)] for _ in range(9)]
        
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j]==".":
        #             possible_solutions[i][j] = {"1","2","3","4","5","6","7","8","9"} - (occupations_3x3[i//3][j//3] | occupations_h[i] | occupations_v[j])
        #             print("possible_solutions["+str(i)+"]["+str(j)+"]", possible_solutions[i][j])
        #             # print("possible_solutions["+str(i)+"]["+str(j)+"]")#, possible_solutions[i][j])
        #             # print(occupations_3x3[i//3][j//3])
        #             # print(occupations_h[i])
        #             # print(occupations_v[j])
        #             # print(possible_solutions[i][j])
        #         # else:
        #         #     possible_solutions[i][j] = {}





board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

Output= [["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]]

board = [["8",".",".",".",".",".",".",".","."],
        [".",".","3","6",".",".",".",".","."],
        [".","7",".",".","9",".","2",".","."],
        [".","5",".",".",".","7",".",".","."],
        [".",".",".",".","4","5","7",".","."],
        [".",".",".","1",".",".",".","3","."],
        [".",".","1",".",".",".",".","6","8"],
        [".",".","8","5",".",".",".","1","."],
        [".","9",".",".",".",".","4",".","."]]

Output= [["8","1","2","7","5","3","6","4","9"],
        ["9","4","3","6","8","2","1","7","5"],
        ["6","7","5","4","9","1","2","8","3"],
        ["1","5","4","2","3","7","8","9","6"],
        ["3","6","9","8","4","5","7","2","1"],
        ["2","8","7","1","6","9","5","3","4"],
        ["5","2","1","9","7","4","3","6","8"],
        ["4","3","8","5","2","6","9","1","7"],
        ["7","9","6","3","1","8","4","5","2"]]

obj = Solution()
obj.solveSudoku(board)
bad_cells = 0
missing = 0
bad_cells_h = [0 for _ in range(9)]
bad_cells_v = [0 for _ in range(9)]
for i in range(9):
    for j in range(9):
        print(board[i][j]+":"+Output[i][j], end='')
        if board[i][j] != Output[i][j]:
            print(" B\t", end='')
            bad_cells+=1
            bad_cells_h[i]+=1
            bad_cells_v[j]+=1
            if board[i][j] == ".":
                missing+=1
        else:
            print("\t", end='')
        
        if j==9-1:
            # print("\t", end='')
            print(i, "\t", bad_cells_h[i])
    # print()
    if i==9-1:
        print()
        for j in range(9):
            print(str(j)+"\t", end='')
        print()
        print()
        for j in range(9):
            print(str(bad_cells_v[j])+"\t", end='')
print()
print()
print("bad cells:", bad_cells)
print("missing:", missing)