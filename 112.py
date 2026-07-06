from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def find_target(root, targetSum, current, found):
            print(root.val, current)
            if root.left is None and root.right is None and current == targetSum:
                found[0] = True
                return
            if root.left:
                find_target(root.left, targetSum, current+root.left.val, found)
            if root.right:
                find_target(root.right, targetSum, current+root.right.val, found)
        
        found = [False]

        if not root:
            return False

        find_target(root, targetSum, root.val, found)
        return found[0]


root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
# root = [1,2,3, 2, 4, None, None, 5, 6, None, 8, 11, 12, 14, 15, 16, 17]
# root = [5,4,8,11,None,13,4,7,2,1,2,None,1]

targetSum = 22

root = [1,2,3]
targetSum = 5

root = []
targetSum = 0

root = [1,2]
targetSum = 1



from collections import deque


# if len(root) != 0:
#     root_node = TreeNode(root[0])
#     queue = deque([root_node])
#     i=1
#     while queue:
#         node = queue.popleft()
#         if node:
#             children = []
#             # children = [TreeNode(root[i]) if root[i] is not None else None, TreeNode(root[i+1]) if root[i+1] is not None else None]
#             children.append(TreeNode(root[i]) if root[i] is not None else None)
#             i+=1

#             children.append(TreeNode(root[i]) if root[i] is not None else None)
#             i+=1
#             print("node", node.val)
#             print("c",[c.val if c is not None else None for c in children])
#             node.left, node.right = children
#             # queue.extend([c for c in children if c is not None])
#             queue.extend(children)
#             i+=2
#             if i == len(root):
#                 break
# else:
#     root_node = None


def array_to_binary_tree(lst):
    if not lst:
        return
    values = iter(lst)
    root = TreeNode(next(values))
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            # Get next two values from input list, and 
            #   if they are not None, create a node for them
            children = [
                None if value is None else TreeNode(value)
                for value in (next(values, None), next(values, None))
            ]
            # Append these two to the queue, and also attach them in the tree
            queue.extend(children)
            node.left, node.right = children

    return root

root_node = array_to_binary_tree(root)

print("---------------")
print("---------------")
print("---------------")
obj = Solution()
print(obj.hasPathSum(root_node, targetSum))









# root_good = []
# total_bottom_leafs = deque()
# bottom_leafs = [root[0]]
# before_iter = 1
# i=0

# root_node = TreeNode(root[0])
# upcomming_to_children = deque([root_node])

# while True:
#     start_iter = before_iter
#     bottom_leafs = [b for b in bottom_leafs if b]
#     end_iter = start_iter+len(bottom_leafs)*2

#     bottom_leafs = [root[j] for j in range(start_iter, end_iter)]
#     before_iter = start_iter+len(bottom_leafs)
#     print(bottom_leafs, before_iter, len(root))



#     d = bottom_leafs
#     print(d)
#     i=0
#     utcn = len(upcomming_to_children)
#     for j in range(utcn):
#         utc = upcomming_to_children.popleft()
#         print("d[i]", d[i])
#         if d[i]:
#             utc.left = TreeNode(d[i])
#             upcomming_to_children.append(utc.left)
#             print("utc",utc.val, utc.left.val)
#         i+=1
#         print("d[i]", d[i])
#         if d[i]:
#             utc.right = TreeNode(d[i])
#             upcomming_to_children.append(utc.right)
#             print("utc",utc.val, utc.right.val)
#         i+=1
#     print("-")

#     if before_iter == len(root):
#         break


# root[0] = TreeNode(root[0])
# for i,n in enumerate(root):
#     if n is None: continue
#     root[i] = TreeNode(n)
#     if i%2:
#         root[(i-1)//2].left  = root[i]
#     else:
#         root[(i-1)//2].right = root[i]


print("--------")
def print_tree(node):
    print(node.val)
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)

# print_tree(root[0])
print("r")
print_tree(root_node)







# from collections import deque

# root_good = []
# total_bottom_leafs = deque()
# bottom_leafs = [root[0]]
# before_iter = 1
# i=0
# while True:
#     new_bottom_leafs = []
#     start_iter = before_iter
#     bottom_leafs = [b for b in bottom_leafs if b]
#     end_iter = start_iter+len(bottom_leafs)*2

#     bottom_leafs = [root[j] for j in range(start_iter, end_iter)]
#     before_iter = start_iter+len(bottom_leafs)
#     print(bottom_leafs, before_iter, len(root))
#     total_bottom_leafs.append(bottom_leafs)

#     if before_iter == len(root):
#         break

# print("t", total_bottom_leafs)

# import copy

# root_node = TreeNode(root[0])
# upcomming_to_children = deque([root_node])

# while len(total_bottom_leafs)!=0:
#     d = total_bottom_leafs.popleft()
#     print(d)
#     i=0
#     utcn = len(upcomming_to_children)
#     for j in range(utcn):
#         utc = upcomming_to_children.popleft()
#         print("d[i]", d[i])
#         if d[i]:
#             utc.left = TreeNode(d[i])
#             upcomming_to_children.append(utc.left)
#             print("utc",utc.val, utc.left.val)
#         i+=1
#         print("d[i]", d[i])
#         if d[i]:
#             utc.right = TreeNode(d[i])
#             upcomming_to_children.append(utc.right)
#             print("utc",utc.val, utc.right.val)
#         i+=1
#     print("-")
# print("--------")
# def print_tree(node):
#     print(node.val)
#     if node.left:
#         print_tree(node.left)
#     if node.right:
#         print_tree(node.right)

# print_tree(root_node)
