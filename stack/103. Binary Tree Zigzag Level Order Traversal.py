class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        s = [root]
        lv = 0
        while len(s):
            nodeList = []
            while len(s):
                node = s.pop(0)
                nodeList.append(node)
            ret.append([n.val for n in nodeList])
            if lv % 2 == 1:
                ret[-1].reverse()
            for node in nodeList:
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
            lv += 1
        return ret

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
print Solution().zigzagLevelOrder(root)