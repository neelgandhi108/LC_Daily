# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        children = set()
        for parent,child,isLeft in descriptions:
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            if child not in node_map:
                node_map[child] = TreeNode(child)
            if bool(isLeft):
                node_map[parent].left =  node_map[child]
            else:
                node_map[parent].right = node_map[child]
            children.add(child)
        for node in node_map.values():
            if node.val not in children:
                return node
        return None