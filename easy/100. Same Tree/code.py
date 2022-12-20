# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if(p and q):
            if p.val!=q.val:
                print("p !=",p)
                print("q !=",q)
                return False
            else:
                print(p)
                print(q)
                teste_p = self.isSameTree(p.left,q.left)
                teste_q = self.isSameTree(p.right,q.right)
                if(teste_p == False or teste_q == False):
                    return False
        elif(p or q):
            print("elif")
            print(p,q)
            return False
            

        return True    
            