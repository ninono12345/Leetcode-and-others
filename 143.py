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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # final_heads = []

        # def return_from_last(head, final_heads):
        #     if not head.next:
        #         final_heads.append(head)
        #         return head
            
        #     last = return_from_last(head.next, final_heads)

        #     final_heads.append(head)
        
        # return_from_last(head, final_heads)

        final_heads = []
        curr = head
        while curr:
            final_heads.append(curr)
            
            curr=curr.next


        for h in final_heads:
            print(h.val)
        
        # if head == head:
        #     print("yes")
        print("before")
        print_linked_list(head)

        node = head
        i=0
        while True:
            last_node = final_heads.pop()
            if last_node==node or last_node == node.next:
                last_node.next=None
                break
            temp = node.next
            node.next=last_node
            last_node.next=temp
            node=temp


        print("-")
        print_linked_list(head)
        # def rll(head):
        #     if not head or not head.next:
        #         return head
            
        #     tail = rll(head.next)

        #     head.next.next = head
        #     head.next = None

        #     return tail
        
        # tail = rll(head)

        # print_linked_list(tail)



head = [1,2,3,4, 5, 6, 7, 8]
# head = [1,2,3,4]

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
# print_linked_list(obj.reorderList(ll))
obj.reorderList(ll)