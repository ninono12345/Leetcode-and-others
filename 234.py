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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid, tail = head, head

        single_mid=True
        while tail.next:
            if tail.next.next:
                mid = mid.next
                tail = tail.next.next
            else:
                tail = tail.next
                single_mid=False

        # print(mid.val, tail.val, single_mid)
        if single_mid:
            # print("this1")
            new_mid = ListNode(mid.val, mid.next)
        else:
            # print("this2")
            new_mid = mid.next
        mid.next = None
        # print()
        # print_linked_list(head)
        # print()
        # print_linked_list(new_mid)
        # print()

        prev = None
        curr = new_mid
        tail = None

        while curr:
            # print("c", curr.val, curr.next.val)
            tail = curr.next
            curr.next = prev
            prev = curr
            # print("p", prev.val)
            curr = tail
        
        # print_linked_list(prev)

        while head and prev:
            if head.val == prev.val:
                head = head.next
                prev = prev.next
            else:
                return False
        
        return True



head = [1,2,2,1]
head = [1,2,3, 4, 4, 3, 2, 1]


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



# def print_linked_list(ll):
#     if not ll:
#         return
#     node = ll
#     print(node.val)
#     while node.next:
#         node=node.next
#         print(node.val)

# print_linked_list(ll)



obj = Solution()
# print_linked_list(obj.reverseList(ll))
print(obj.isPalindrome(ll))