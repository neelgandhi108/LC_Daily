class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        q = deque([root])
        level_index = 0

        while q:
            prev_val = None
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                # **Even level**: Values must be **odd** and **strictly increasing**
                if level_index % 2 == 0:
                    if node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val):
                        return False
                # **Odd level**: Values must be **even** and **strictly decreasing**
                else:
                    if node.val % 2 != 0 or (prev_val is not None and node.val >= prev_val):
                        return False
                prev_val = node.val
                # Add children to queue for next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_index += 1

        return True