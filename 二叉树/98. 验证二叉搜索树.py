from typing import Optional

# 中序遍历
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def zhongxu(self,root:TreeNode):
        if root.left!=None:
            self.zhongxu(root.left)
        self.res.append(root.val)
        if root.right!=None:
            self.zhongxu(root.right)
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.zhongxu(root)
        lst=self.res
        for i in range(len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False
        return True
            
            