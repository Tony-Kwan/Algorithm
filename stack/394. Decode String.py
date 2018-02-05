class Node(object):
    def __init__(self, k, s):
        self.k = k
        self.s = s
        self.child = []

    def __str__(self):
        return '(%d, %s)' % (self.k, self.s)

class Solution(object):
    def decodeString(self, s):
        if not s or len(s) == 0:
            return ''
        s = '1[' + s + ']'
        result = self.getSub(s)
        root = result[0]
        self.build(root)
        return self.postOrder(root)

    def build(self, node):
        restStr = node.s
        while 1:
            result = self.getSub(restStr)
            child = result[0]
            restStr = result[1]
            node.child.append(child)
            if not self.isDecodedStr(child.s):
                self.build(child)
            if restStr == '':
                break

    def getSub(self, s):
        idx = s.find('[')
        if s[0] > '9':
            if idx != -1:
                return Node(1, s[0]), s[1:]
            else:
                return Node(1, s), ''
        n = len(s)
        k = int(s[:idx])
        st = []
        for i in xrange(idx, n):
            st.append(s[i])
            if s[i] == ']':
                tmp = []
                while 1:
                    tmp.append(st.pop())
                    if tmp[-1] == '[':
                        tmp.reverse()
                        st.append(''.join(tmp))
                        break
                if len(st) == 1:
                    break
        return Node(k, st[0][1:-1]), s[i + 1:]

    def isDecodedStr(self, s):
        return s.find('[') == -1

    def postOrder(self, node):
        one = ''
        if len(node.child):
            for child in node.child:
                one += self.postOrder(child)
        else:
            one = node.s
        return one * node.k

print Solution().decodeString("3[a]2[bc]")        #aaabcbc
print Solution().decodeString("3[a2[c]]")           #accaccacc
print Solution().decodeString("2[abc]3[cd]ef2[a]")      #abcabccdcdcdef