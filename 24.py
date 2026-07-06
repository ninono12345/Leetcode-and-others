from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(ll):
    if not ll:
        return
    node = ll
    print(node.val)
    while node.next:
        node=node.next
        print(node.val)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # print("start--")
        # print_linked_list(head)
        
        # new_head = head.next
        # head.next = head.next.next
        # new_head.next = head
        # # print("-")
        # # print_linked_list(new_head)

        # new_head.next.next = self.swapPairs(new_head.next.next)

        # # print("finish--")
        # # print_linked_list(new_head)
        # return new_head
        final_head = head.next
        # current = head
        prev=None
        
        while head and head.next:
            new_head = head.next
            head.next = head.next.next
            new_head.next = head
            # print("new_head", new_head.val)
            if prev:
                prev.next=new_head
            head = new_head.next.next
            prev = new_head.next
            # print("prev", prev.val)
            # print("head", head.val)

        return final_head



head = [1,2,3,4]

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

print_linked_list(ll)
print()
# print_linked_list(ll2)

obj = Solution()
print_linked_list(obj.swapPairs(ll))