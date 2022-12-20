# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        obj = head
        new_list = []
        frente = ""
        tras = ""
        for i in range(9999999999):
            try:
                new_list.append(obj.val)
                obj = obj.next
            except Exception as e:
                break
                
        for i in range(len(new_list)):
            frente += str(new_list[i])
            tras += str(new_list[-(i+1)])
                    
        print(new_list)
        
        return tras == frente
            
        
     