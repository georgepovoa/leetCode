# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while(current is not None):
            print("antigo -current ",current)
            print("antigo - prev ", prev)
            next = current.next
            print("next",next)
            current.next = prev
            print("current.next ",current.next)
            prev = current
            print("novo - prev ",prev)
            current = next
        head = prev
    
        return head
        
