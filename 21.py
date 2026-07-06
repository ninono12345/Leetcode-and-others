from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        if not list1 or not list2:
            return list1 if list1 else list2
        if not node1 and not node2:
            return None
        if node1.val<node2.val:
            ret = ListNode(node1.val)
            node1 = node1.next
        else:
            ret = ListNode(node2.val)
            node2 = node2.next
        rn = ret

        while node1 or node2:
            while not node1 and node2:
                rn.next = ListNode(node2.val)
                rn = rn.next
                node2 = node2.next

            while node1 and not node2:
                rn.next = ListNode(node1.val)
                rn = rn.next
                node1 = node1.next

            if node1 and node2:
                if node1.val<node2.val:
                    rn.next = ListNode(node1.val)
                    rn = rn.next
                    node1 = node1.next
                else:
                    rn.next = ListNode(node2.val)
                    rn = rn.next
                    node2 = node2.next
        return ret

        # if not list1 or not list2:
        #     return list1 if list1 else list2
        
        # if list1.val>list2.val:
        #     list1, list2 = list2, list1

        # list1.next = self.mergeTwoLists(list1.next, list2)

        # return list1

        

list1 = [1,2,4]
list2 = [1,3,4]

def generate_linked_list(l):
    if len(l) == 0:
        return None
    
    ll = ListNode(l[0])
    node = ll
    for i in range(1, len(l)):
        node.next = ListNode(l[i])
        node = node.next
    
    return ll

ll1 = generate_linked_list(list1)
ll2 = generate_linked_list(list2)

# print(max(ll1, ll2, key=lambda x: x.val).val)

# print(ll1.val)
# print(ll1.next.val)
# print(ll1.next.next.val)


def print_linked_list(ll):
    if not ll:
        return
    node = ll
    print(node.val)
    while node.next:
        node=node.next
        print(node.val)

# print_linked_list(ll1)

obj = Solution()
print_linked_list(obj.mergeTwoLists(ll1, ll2))