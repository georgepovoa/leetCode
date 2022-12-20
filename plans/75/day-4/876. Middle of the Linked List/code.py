# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) :
        
        obj = head
        size =1
        i = 1

        while(obj.next != None):
            size +=1
            obj = obj.next
          
        if size%2 ==1:
            print(size)
            while(i<=size):
                if i == int((size/2) + 0.5):
                    return head
                head = head.next
                i+=1
        else:
            print(size)

            while(i<=size):
                if i == (size/2) + 1 :
                    return head
                head = head.next
                i+=1

        return head