# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = [[]]
        depth = 0
        def recursion(root,depth):
            if root == None:
                return 0
            
            recursion(root.left,depth+1)
            recursion(root.right,depth+1)
           
        
            while(True):
                try:
                    result[depth].append(root.val)
                    break
                except:
                    result.append([])
                
            
        recursion(root,depth)
        if result == [[]]:
            result = []
        return (result)
            
            
            
        