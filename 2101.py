from typing import List
from math import sqrt
# import networkx as nx

# class Solution:
#     def maximumDetonation(self, bombs: List[List[int]]) -> int:
#         length = len(bombs)
#         # x_distances = [i1 for i1, i2, i3 in bombs]
#         # y_distances = [i2 for i1, i2, i3 in bombs]
#         # print(x_distances)
#         # print(y_distances)
#         # i_distances = list(range(len(bombs)))
#         # i_distances = [i for i in sorted(i_distances, key=lambda x: x_distances[x] - y_distances[x])]
#         # print(i_distances)

#         # graph = [[]]*length

#         # for i in range(length):
#         #     for j in range(length):

#         graph = nx.Graph()

#         strengths = [i3 for i1, i2, i3 in bombs]
#         # print("ss",strengths)
#         # for i in range(length):
#         #     graph.add_node(i, strength=bombs[i][2])
#         for i in range(length-1):
#             for j in range(i+1, length):
#                 x = abs(bombs[i][0] - bombs[j][0])
#                 y = abs(bombs[i][1] - bombs[j][1])
#                 # distance = sqrt(x**2 + y**2)
                
#                 graph.add_edge(i, j, weight=sqrt(x**2 + y**2))

        
#         # for n, s in graph.nodes(data=True):
#         #     print(n, s)

#         # for e1, e2, w in graph.edges(data=True):
#         #     print(e1, e2, w)
        
                

#         # print(graph)
#         # print()
#         final_destructed_nodes=[]
#         for i in range(0, length):
#             destructed_nodes=[]
#             def dfs(node, destructed_nodes):
#                 destructed_nodes.append(node)
#                 edges = graph.edges(node, data=True)
#                 # print(edges)
#                 # for e in edges:
#                 #     print(e)
#                 edges = sorted(edges, key=lambda x: x[2]["weight"])
#                 # print("-")
#                 # for e in edges:
#                 #     print(e)
#                 # print()
#                 # print()
                
#                 for e1, e2, e3 in edges:
#                     # print("e1", e1, "e2", e2, "e3", e3, strengths[node])
#                     if e3["weight"]<=strengths[node]:
#                         if e2 not in destructed_nodes:
#                             dfs(e2, destructed_nodes)
#                     else:
#                         break
            
#             dfs(list(graph)[i], destructed_nodes)
#             if len(destructed_nodes)>len(final_destructed_nodes):
#                 final_destructed_nodes = destructed_nodes
#             # final_destructed_nodes = max(final_destructed_nodes, destructed_nodes)
#             # break
#         return final_destructed_nodes
            

        # for i in range(0, length):
        #     print(i)
        #     past_bombs = []
        #     def dfs(bomb_i):
        #         past_bombs.append(bomb_i)

        #         if bomb_i-1 >= 0 and bomb_i-1 not in past_bombs:
        #             x = abs(bombs[bomb_i-1][0] - bombs[bomb_i][0])
        #             y = abs(bombs[bomb_i-1][1] - bombs[bomb_i][1])
        #             if sqrt(x**2 + y**2) <= bombs[bomb_i][2]:
        #                 print("sqrt1", sqrt(x**2 + y**2), x, y, bombs[bomb_i], bomb_i)
        #                 dfs(bomb_i-1)
                
        #         if bomb_i+1 < length and bomb_i+1 not in past_bombs:
        #             x = abs(bombs[bomb_i+1][0] - bombs[bomb_i][0])
        #             y = abs(bombs[bomb_i+1][1] - bombs[bomb_i][1])
        #             if sqrt(x**2 + y**2) <= bombs[bomb_i][2]:
        #                 print("sqrt2", sqrt(x**2 + y**2))
        #                 dfs(bomb_i+1)
            
        #     dfs(i)
        #     break
        # print(past_bombs)
                    
                    

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        length = len(bombs)

        strengths = [i3 for i1, i2, i3 in bombs]

        # graph = [[0]*length]*length
        graph = [[0] * length for _ in range(length)]

        cnt=0
        for i in range(length):
            for j in range(0, length):
                # print(i, j)
                x = abs(bombs[i][0] - bombs[j][0])
                y = abs(bombs[i][1] - bombs[j][1])
                distance = sqrt(x**2 + y**2)
                # print(distance, strengths[i])
                # graph[i][j] = distance
                if distance<=strengths[i]:
                    graph[i][j] = 1
                    # graph[j][i] = 1
                # else:
                #     graph[i][j] = 0
                #     graph[j][i] = 0

        # print(graph)
        # for g in graph:
        #     print(g)
        # print("-")
        
        final_past_bombs = []
        for i in range(0, length):
            past_bombs = []
            def dfs(bomb_i):
                past_bombs.append(bomb_i)

                good_bombs = [i for i in range(length) if graph[bomb_i][i]==1]
                # print("gb", good_bombs)

                for gb in good_bombs:
                    if gb not in past_bombs:
                        # print("g",gb)
                        dfs(gb)
                
            dfs(i)
            # print(past_bombs)
            if len(past_bombs) > len(final_past_bombs):
                final_past_bombs = past_bombs
            # break
        
        return len(final_past_bombs)



# bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
# bombs = [[1,1,5],[10,10,5]]
# bombs = [[2,1,3],[6,1,4]]
# bombs = [[2,1,3],[6,1,4]]
bombs = [[4,4,3],[4,4,3]]

obj = Solution()
print()
print(obj.maximumDetonation(bombs))


