class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None or root.left == None and root.right == None:
            return
        
        if root.left != None:
            self.flatten(root.left)
            
            tmp_right = root.right
            root.right = root.left
            root.left = None
            
            t = root.right
            while t.right != None:
                t = t.right
            
            t.right = tmp_right
            
        self.flatten(root.right)
