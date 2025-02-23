# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        def backtrack(n):
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode(0)]
            if n in dp:
                return dp[n]
            res = []
            for l in range(n):
                r =  n -l -1
                leftSubTrees , rightSubTrees = backtrack(l) , backtrack(r)
                for leftSubTree in leftSubTrees:
                    for rightSubTree in rightSubTrees:
                        res.append(TreeNode(0,leftSubTree,rightSubTree))
            dp[n] = res
            return res
        return backtrack(n)