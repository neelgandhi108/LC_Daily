class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        N = len(postorder)
        post_val_to_idx = {} # val -> idx

        for i,n in enumerate(postorder):
            post_val_to_idx[n] = i
        def build(preorder_i1,preorder_i2,postorder_j1,postorder_j2):
            if preorder_i1>preorder_i2 or postorder_j1>postorder_j2:
                return None
            root = TreeNode(preorder[preorder_i1])
            if preorder_i1 != preorder_i2:
                left_val = preorder[preorder_i1+1]
                mid = post_val_to_idx[left_val]
                left_size = mid - postorder_j1 + 1
                root.left = build(preorder_i1+1,preorder_i1+left_size,postorder_j1,mid)
                root.right = build(preorder_i1+left_size+1,preorder_i2,mid+1,postorder_j2-1)
            return root
        return build(0,N-1,0,N-1)