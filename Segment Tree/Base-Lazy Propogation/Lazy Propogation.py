class SegmentTree:
    def __init__(self,arr):
        self.n = len(arr)
        self.seg = [0]*(4*self.n)
        self.lazy = [0]*(4*self.n)
        self.build(0,0,self.n-1,arr)

    def build(self,idx,low,high,arr):
        if low == high:
            self.seg[idx] = arr[low]
            return
        mid = (low+high) // 2
        self.build(2*idx+1,low,mid,arr)
        self.build(2*idx+2,mid+1,high,arr)
        self.seg[idx] = self.seg[2*idx+1] + self.seg[2*idx+2]

    def range_update(self,idx,low,high,l,r,val):
        if self.lazy[idx] != 0:
            self.seg[idx] += (high-low+1)*self.lazy[idx]
            if low != high:
                self.lazy[2*idx+1] += self.lazy[idx]
                self.lazy[2*idx+2] += self.lazy[idx]
            self.lazy[idx] = 0
        if r < low or l > high:
            return
        if low >= l and high <= r:
            self.seg[idx] += (high-low+1) * val
            if low != high:
                self.lazy[2*idx+1] += val
                self.lazy[2*idx+2] += val
            return
        mid = (low + high) // 2
        self.range_update(2*idx+1,low,mid,l,r,val)
        self.range_update(2*idx+2,mid+1,high,l,r,val)
        self.seg[idx] = self.seg[2*idx+1] + self.seg[2*idx+2]

    def query_sum_lazy(self,idx,low,high,l,r):
        if self.lazy[idx] != 0:
            self.seg[idx] += (high - low + 1) * self.lazy[idx]
            if low != high:
                self.lazy[2 * idx + 1] += self.lazy[idx]
                self.lazy[2 * idx + 2] += self.lazy[idx]
            self.lazy[idx] = 0

        if r < low or l > high:
            return 0

        if low >= l and high <= r:
            return self.seg[idx]

        mid = (low + high) // 2
        return self.query_sum_lazy(2 * idx + 1, low, mid, l, r) + \
               self.query_sum_lazy(2 * idx + 2, mid + 1, high, l, r)