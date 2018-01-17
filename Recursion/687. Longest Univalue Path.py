class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ans = 0

    def longestUnivaluePath(self, root):
        self.travel(root)
        return self.ans

    def travel(self, node):
        if node == None:
            return -1
        lv = self.travel(node.left)
        rv = self.travel(node.right)
        if node.left != None and node.right != None:
            if node.val == node.left.val and node.val == node.right.val:
                self.ans = max(self.ans, lv + rv + 2)
                return max(lv, rv) + 1
            elif node.val == node.left.val:
                self.ans = max(self.ans, lv + 1)
                return lv + 1
            elif node.val == node.right.val:
                self.ans = max(self.ans, rv + 1)
                return rv + 1
            else:
                return 0
        if node.left != None:
            if node.val == node.left.val:
                self.ans = max(self.ans, lv + 1)
                return lv + 1
            else:
                return 0
        if node.right != None:
            if node.val == node.right.val:
                self.ans = max(self.ans, rv + 1)
                return rv + 1
            else:
                return 0
        return 0

# [5,4,5,1,1,5]
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)
print Solution().longestUnivaluePath(root)

# [1,4,5,4,4,5]
root2 = TreeNode(1)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(5)
print Solution().longestUnivaluePath(root2)

# [1,1,1,1,1,1]
root3 = TreeNode(1)
root3.left = TreeNode(1)
root3.right = TreeNode(1)
root3.left.left = TreeNode(1)
root3.left.right = TreeNode(1)
root3.right.left = TreeNode(1)
print Solution().longestUnivaluePath(root3)