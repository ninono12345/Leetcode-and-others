from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(head, prev, tail):
            if not head.next:
                tail[0] = head
                # return
            else:
                rec(head.next, head, tail)

            # print(prev.val, head.val)
            head.next = prev

        tail = [None]
        if not head:
            return None
        if not head.next:
            return head
        rec(head.next, head, tail)
        head.next=None

        return tail[0]

        # if not head or not head.next:
        #     return head
        
        # tail = self.reverseList(head.next)

        # head.next.next = head
        # head.next = None

        # return tail
    






head = [1,2,3,4,5]

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
print_linked_list(obj.reverseList(ll))
# obj.reverseList(ll)
# print(cnt)