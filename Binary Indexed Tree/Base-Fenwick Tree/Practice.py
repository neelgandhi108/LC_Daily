class FenwickTree:
    def __int__(self,n):
        self.n = n
        self.fen = [0]*(n+1)

    def update(self,i,add):
        while i < self.n:
            self.fen[i] += add
            # Key operations i += (i &-i)
            # Add rightmost set bit to i
            i += (i & -i)

    def sum(self,i):
        s = 0
        while i > 0:
            s += self.fen[i]
            # Key operations i -= (i &-i)
            # Remove rightmost set bit from i
            i -= (i & -i)
        return s

    def range_sum(self,left,right):
        return self.sum(right) - self.sum(left)

    def get_value(self,i):
        if i == 0:
            return 0
        return self.range_sum(i,i)
