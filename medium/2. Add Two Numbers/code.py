# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_of_values_1 = []
        list_of_values_2 = []
        while(True):
            list_of_values_1.insert(0,l1.val)
            l1 = l1.next
            try:
                if l1.next == None:
                
                    list_of_values_1.insert(0,l1.val)
                    break
            except:
                break
        while(True):
            list_of_values_2.insert(0,l2.val)
            l2 = l2.next
            try:
                if l2.next == None:
                    list_of_values_2.insert(0,l2.val)
                    break
            except:
                break
        list_of_values_1 = int("".join(str(e) for e in list_of_values_1))
        list_of_values_2 = int("".join(str(e) for e in list_of_values_2))
        result =str(list_of_values_1 + list_of_values_2)[::-1]
        list_of_nodes = []
        i = 1
        for i in range(len(result)):
            list_of_nodes.append(ListNode(val = int(result[i])))
        for i in range(len(list_of_nodes)-1):
            list_of_nodes[i].next = list_of_nodes[i+1]  
        return list_of_nodes[0]            