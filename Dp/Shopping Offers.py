INF = 1 << 30

class Solution(object):
    n = 0
    l0 = []
    d = {}

    def shoppingOffers(self, price, special, needs):
        self.n = len(price)
        if self.n == 0:
            return 0
        self.l0 = [0] * self.n

        for i in xrange(self.n):
            l = [1 if j == i else 0 for j in xrange(self.n)]
            l.append(price[i])
            special.append(l)
        # print special

        return self.f(special, needs)
        

    def f(self, special, l):
        if l == self.l0:
            return 0
        if min(l) < 0:
            return INF
        t = tuple(l)
        if t not in self.d:
            self.d[t] = INF
        for s in special:
            tmp = [l[i] - s[i] for i in xrange(self.n)]
            self.d[t] = min(self.d[t], self.f(special, tmp) + s[-1])
        return self.d[t]



print Solution().shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2])   #14
print Solution().shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]) #11
print Solution().shoppingOffers([1,1,1], [[1,1,0,0],[2,2,1,0]], [1,1,1]) #1