from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # s1 = ""
        # s2 = ""

        # while l1:
        #     s1 = str(l1.val)+s1
        #     l1 = l1.next
        
        # while l2:
        #     s2 = str(l2.val)+s2
        #     l2 = l2.next
        
        # print(s1, s2)

        # ans = list(str(int(s1)+int(s2)))
        # print(ans)

        # ret = ListNode(ans.pop())
        # node = ret
        # while ans:
        #     # a = ans
        #     node.next = ListNode(ans.pop())
        #     node = node.next

        # return ret

        def rll(head):
            if not head or not head.next:
                return head
            
            tail = rll(head.next)

            head.next.next = head
            head.next = None

            return tail
        
        l1 = rll(l1)
        l2 = rll(l2)

        s1 = ""
        s2 = ""

        while l1:
            s1+=str(l1.val)
            l1=l1.next
        
        while l2:
            s2+=str(l2.val)
            l2=l2.next
        
        # ans = (str(int((s1))+int((s2))))
        # print((ans))
        ans = list(str(int(s1)+int(s2)))         # after
        ret = ListNode(int(ans.pop()))
        node = ret
        while ans:
            node.next = ListNode(int(ans.pop()))
            node = node.next
        return ret




l1 = [2,4,3]
l2 = [5,6,4]

def generate_linked_list(l):
    if len(l) == 0:
        return None
    
    ll = ListNode(l[0])
    node = ll
    for i in range(1, len(l)):
        node.next = ListNode(l[i])
        node = node.next
    
    return ll

ll1 = generate_linked_list(l1)
ll2 = generate_linked_list(l2)

def print_linked_list(ll):
    if not ll:
        return
    node = ll
    print(node.val)
    while node.next:
        node=node.next
        print(node.val)

# print_linked_list(ll1)
# print_linked_list(ll2)

obj = Solution()
print_linked_list(obj.addTwoNumbers(ll1, ll2))