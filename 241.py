from typing import List
import json
# import networkx as nx

def get_grouping(graph1, graph2, ending=False):
    # if len(graph1)==3:
    #     return [[[graph1[0], graph1[1]], graph1[2]], [graph1[0], [graph1[1], graph1[2]]]]
    if len(graph1)==1:
        # return graph1, True
        if ending:
            return [graph2[graph1[0]-1], int(graph1[0])], False
        else:
            return [int(graph1[0]), graph2[graph1[0]]], False
    # if len(graph1)==2:
    #     return [graph1[0], graph1[1]]
    # print(graph1)
    if len(graph1) <=2:
        # return [graph1], True
        return [[int(graph1[0]), graph2[graph1[0]], int(graph1[1])]], True
    
    new_graph = []
    for i in range(1, len(graph1)):
        # print(graph1[0:i])
        # print(graph1[i:len(graph1)])
        # print("--")
        grouping1, out1 = get_grouping(graph1[0:i], graph2, False)
        grouping2, out2 = get_grouping(graph1[i:len(graph1)], graph2, True)
        to_append = grouping1
        if out1:
            if isinstance(grouping1[0], int):
                to_append.append(graph2[grouping1[0]])
            elif isinstance(grouping1[0], list):
                to_append.append(graph2[grouping1[0][2]])
        to_append += grouping2
        new_graph.append(to_append)
    
    return new_graph, False

def get_grouping2(graph):
    # if len(graph)==1:
        # print("r")
    if len(graph)==2:
        return graph

    if len(graph) <=3:
        return [graph]
    
    new_graph = []
    for i in range(2, len(graph)-1):
        new_graph.append(get_grouping2(graph[0:i])+get_grouping2(graph[i:len(graph)]))
    
    return new_graph

def get_grouping3(graph1):
    if len(graph1)==1:
        return [graph1[0]], False
    if len(graph1) <=2:
        return [graph1], False
    
    new_graph = []
    for i in range(1, len(graph1)):
        grouping1, out1 = get_grouping3(graph1[0:i])
        grouping2, out2 = get_grouping3(graph1[i:len(graph1)])
        # print("--------1")
        # print(grouping1)
        # print("--------2")
        # print(grouping2)
        # print(len(grouping1), len(grouping2))
        # if len(grouping1)>2:
        #     print(json.dumps(grouping1, indent=4))
        # if len(grouping2)>2:
        #     print(json.dumps(grouping2, indent=4))
        to_append = []

        if not out1 and not out2:

            to_append.append(grouping1+grouping2)
        if out1 and not out2:
            for g in grouping1:
                to_append.append([g]+grouping2)
        #     to_append.append([grouping1[0]]+grouping2)
        #     to_append.append([grouping1[1]]+grouping2)
        if not out1 and out2:
            for g in grouping2:
                to_append.append(grouping1+[g])
        #     to_append.append(grouping1+[grouping2[0]])
        #     to_append.append(grouping1+[grouping2[1]])
        if out1 and out2:
            for g1 in grouping1:
                for g2 in grouping2:
                    to_append.append([g1]+[g2])
        #     print("YES!!!!!!!")
        #     to_append.append(grouping1[0]+grouping2[0])
        #     to_append.append(grouping1[0]+grouping2[1])
        #     to_append.append(grouping1[1]+grouping2[0])
        #     to_append.append(grouping1[1]+grouping2[1])
        #     print(json.dumps(to_append, indent=4))
        # print(json.dumps(to_append, indent=4))
        # to_append.append()

        new_graph += to_append
        # new_graph.append(to_append)
        # new_graph.append(grouping1+grouping2)
        # new_graph.append(grouping1)
        # new_graph.append(grouping2)
        # new_graph.append(out1)
        # new_graph.append(out2)

    return new_graph, True

def get_list_max_depth(grouped):
    has_lists = False
    max_depth = 0
    for g in grouped:
        # print(g)
        if isinstance(g, list):
            has_lists = True
            max_depth = max(max_depth, get_list_max_depth(g))

    
    if has_lists:
        return max_depth+1
    else:
        return 0

def recursive_addition(grouped, graph1, graph2, first=True, request_to_get_low=True):
    # print(grouped)
    # total_sums = []
    cur_sum = 0
    ast = 0
    if isinstance(grouped[0], int):
        int1 = int(graph1[grouped[0]])
        ast = graph2[grouped[0]]
        out_ast_upper = graph2[grouped[0]-1]
    else:
        int1, out_ast1_upper, out_ast1_lower = recursive_addition(grouped[0], graph1, graph2, True)
        # if request_to_get_low:
        out_ast_upper = out_ast1_upper
        ast = out_ast1_lower
        # else:


    if isinstance(grouped[1], int):
        int2 = int(graph1[grouped[1]])
        ast = graph2[grouped[1]-1]
        if grouped[1]<len(graph2):
            out_ast_lower = graph2[grouped[1]]
        else:
            out_ast_lower = -1
    else:
        int2, out_ast2_upper, out_ast2_lower = recursive_addition(grouped[1], graph1, graph2, False)
        ast = out_ast2_upper
        out_ast_lower = out_ast2_lower
    # for i in range(len(grouped)):
    # if isinstance(grouped[0], int) and isinstance(grouped[1], int):

    # if ast==0:
    #     ast = 

    if ast == "+":
        cur_sum=int1+int2
    if ast == "-":
        cur_sum=int1-int2
    if ast == "*":
        cur_sum=int1*int2
    
    # if first:
    #     ast = graph2[int2[0]]
    # else:
    #     ast = graph2[int1[0]-1]
    
    return cur_sum, out_ast_upper, out_ast_lower

# def recursive_addition(grouped, graph1, graph2):

    


# def graph_fixer(grouped):
#     for i in range(len(grouped)):



class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # graph = nx.Graph()
        # for i in range(0, len(expression), 2):
        #     print(i)
        #     graph.add_node(expression[i])
        
        # # for n in graph:
        # #     print(n)


        graph1 = []
        graph2 = []

        # for i in range(0, len(expression), 2):
        #     # print(i)
        #     graph1.append(expression[i])
        # if len(expression)>1:
        #     for i in range(1, len(expression), 2):
        #         # print(i)
        #         graph2.append(expression[i])

        number = []
        for i in range(len(expression)):
            if expression[i].isnumeric():
                number.append(expression[i])
            else:
                graph1.append("".join(number))
                graph2.append(expression[i])
                number = []
            
            if i == len(expression)-1:
                graph1.append("".join(number))

        # print(graph1)
        # print(graph2)

        if len(graph1)==1:
            return [int(graph1[0])]

        # graph = []
        # for i in range(len(expression)):
        #     if expression[i].isnumeric():
        #         number.append(expression[i])
        #     else:
        #         graph.append("".join(number))
        #         graph.append(expression[i])
        #         number = []
            
        #     if i == len(expression)-1:
        #         graph.append("".join(number))
        
        # print(graph)

        # grouped = get_grouping2(graph)
        # print(grouped)

        indexes = list(range(len(graph1)))

        # grouped, g = get_grouping(indexes, graph2)
        grouped, g = get_grouping3(indexes)
        # print(get_list_max_depth(grouped))
        # # print(grouped)
        # print(json.dumps(grouped, indent=4))
        # print("lg", len(grouped))

        rets = []
        for g in grouped:
        #     while True:
            a1, a2, a3 = recursive_addition(g, graph1, graph2)
            rets.append(a1)
            # break
            # print("r", a1)
        # print(rets)
        return rets
        # for g in grouped:
        #     print(len(g))

        # answers = []

        # for g in grouped:
        #     for i in range(len(g)):


        


obj = Solution()

s1 = "2-1-1"
s1 = "2*3-4*5"
s1 = "99"
# s1 = "9-8+7-6+5-4"
# s1 = "9-8+7-6+5"
# s1 = "0+0+0+0+0*0+0+0*0+0"
# s1 = "99*87-78+66*55-44+33"
# s1 = "12+34-56*78+90"
# s1 = "1+2-3+4-5+6-7+8-9+10"
print(obj.diffWaysToCompute(s1))