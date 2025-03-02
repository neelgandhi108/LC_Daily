class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getSum(node):
            if not node:
                return 0
            return node.val + getSum(node.left) + getSum(node.right)
        totalSum = getSum(root)
        def dfs(node):
            nonlocal totalSum
            if not node:
                return
            dfs(node.left)
            tmp = node.val
            node.val = totalSum
            totalSum -= tmp
            dfs(node.right)
        dfs(root)
        return root