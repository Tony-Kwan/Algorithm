class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        if not n:
            return 0
        l = [(i, heights[i]) for i in xrange(n)]
        i1 = self.get(l)
        l = [(n - i - 1, heights[i]) for i in xrange(n - 1, -1, -1)]
        i2 = self.get(l)
        ans = 0
        for i in xrange(n):
            ans = max(ans, heights[i] * ((n - i2[n - i - 1]) - i1[i]))
        return ans

    def get(self, l):
        ret = []
        s = []
        for it in l:
            idx = it[0]
            val = it[1]
            if len(s) and val > s[-1][1]:
                ret.append(idx)
                s.append(it)
            else:
                while len(s) and val <= s[-1][1]:
                    lastPop = s.pop()
                if not len(s):
                    ret.append(0)
                    s.append(it)
                else:
                    ret.append(lastPop[0])
                    s.append((lastPop[0], val))
        return ret


print Solution().largestRectangleArea([2,1,5,6,2,3])        #10
print Solution().largestRectangleArea([3,6,5,7,4,8,1,0])    #20