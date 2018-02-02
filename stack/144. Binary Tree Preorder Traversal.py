# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret
        s = [root]
        while len(s):
            node = s.pop()
            ret.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return ret

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print Solution().preorderTraversal(root)