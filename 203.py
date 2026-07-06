# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        # print(head.val)
        
        head.next = self.removeElements(head.next, val)
        
        if head.val==val:
            if head.next:
                head = head.next
            else:
                return None
        return head



head = [1,2,6, 6,3,4,5,6]
val = 6
# head = [7,7,7,7]
# val = 7

def generate_linked_list(l):
    if len(l) == 0:
        return None
    
    ll = ListNode(l[0])
    node = ll
    for i in range(1, len(l)):
        node.next = ListNode(l[i])
        node = node.next
    
    return ll

ll = generate_linked_list(head)



def print_linked_list(ll):
    if not ll:
        return
    node = ll
    print(node.val)
    while node.next:
        node=node.next
        print(node.val)

# print_linked_list(ll)



obj = Solution()
print_linked_list(obj.removeElements(ll, val))
# obj.removeElements(ll, val)