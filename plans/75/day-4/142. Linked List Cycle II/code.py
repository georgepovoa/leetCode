# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        list_of_vals = []
        obj = head
        if head == None:
            return head
        while(obj.next!=None):            
            if obj not in list_of_vals:
                list_of_vals.append(obj)
            else:
                for i in range(len(list_of_vals)):
                    if list_of_vals[i] == obj:
                        return obj
            obj = obj.next                    