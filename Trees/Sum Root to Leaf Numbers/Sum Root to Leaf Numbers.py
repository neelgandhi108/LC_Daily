# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node,path_str):
            if not node.left and not node.right:
                res.append(path_str)
                return
            if node.left:   dfs(node.left,path_str+str(node.left.val))
            if node.right:  dfs(node.right,path_str+str(node.right.val))
        res = []
        dfs(root,str(root.val))
        return sum(int(res[i]) for i in range(len(res)))
