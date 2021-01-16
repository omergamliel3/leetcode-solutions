# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []

        def inner(root: TreeNode):
            if root:
                if root.left:
                    inner(root.left)

                res.append(root.val)

                if root.right:
                    inner(root.right)

        inner(root)
        # sort number in acending order
        res = list(sorted(res))
        return res[k-1]
