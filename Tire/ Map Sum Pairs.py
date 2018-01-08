class Node():
    def __init__(self, value):
        self.value = value
        self.child = {}
        

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        node.value += val
        for c in key:
            if c not in node.child:
                node.child[c] = Node(0)
            node = node.child[c]
            node.value += val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for c in prefix:
            if c not in node.child:
                return 0
            node = node.child[c]
        return node.value

obj = MapSum()
obj.insert('apple', 3)
print obj.sum('ap')
obj.insert('app', 2)
print obj.sum('a')