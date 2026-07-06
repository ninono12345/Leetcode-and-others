from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        x_length = len(board)
        y_length = len(board[0])
        found_ships = []
        x = 0
        y = 0
        looked_at = set()
        found_ships_iter = -1
        while True:
            if (x, y) in looked_at:
                if x+1 == x_length:
                    if y+1 == y_length:
                        break
                    x = 0
                    y += 1
                else:
                    x += 1
                continue

            looked_at.add((x, y))
            old_x = x
            old_y = y
            if board[x][y] == "X":
                found_ships_iter+=1
                found_ships.append(1)
                while x-1>=0:
                    if board[x-1][y] == "X":
                        looked_at.add((x-1, y))
                        x -= 1
                        found_ships[found_ships_iter]+=1
                    else:
                        break
                x = old_x
                # y = old_y
                while x+1<x_length:
                    if board[x+1][y] == "X":
                        looked_at.add((x+1, y))
                        x += 1
                        found_ships[found_ships_iter]+=1
                    else:
                        break
                x = old_x
                # y = old_y
                while y-1>=0:
                    if board[x][y-1] == "X":
                        looked_at.add((x, y-1))
                        y -= 1
                        found_ships[found_ships_iter]+=1
                    else:
                        break
                y = old_y
                while y+1<y_length:
                    if board[x][y+1] == "X":
                        looked_at.add((x, y+1))
                        y += 1
                        found_ships[found_ships_iter]+=1
                    else:
                        break
                y = old_y
            # found_ships_iter+=1
            # print(found_ships)
        return len(found_ships)

                        



obj = Solution()
# board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
board = [["X",".","X",".","X"],
         [".","X",".","X","."],
         [".","X",".",".","."],
         [".","X",".",".","X"],
         [".","X",".",".","."],
         ["X",".","X","X","X"],
         [".","X",".",".","."],
         [".","X",".","X","."],
         ["X",".","X",".","X"],
         [".","X",".",".","X"]]
print(obj.countBattleships(board))