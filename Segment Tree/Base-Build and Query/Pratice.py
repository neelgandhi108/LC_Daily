import sys

class SegmemntTree:
    def __init__(self,arr):
        self.n = len(arr)
        self.arr = arr
        self.seg = [0]*(4*self.n)
        self.build(0,0,self.n-1)

    def build(self,idx,low,high):
        if low == high:
            self.seg[idx] = self.arr[low]
            return
        mid = (low+high)//2
        self.build(2*idx+1,low,mid)
        self.build(2*idx+2,mid+1,high)
        self.seg[idx] = max(self.seg[2*idx+1],self.seg[2*idx+2])

    def query(self,idx,low,high,l,r):
        if low >= l and r >= high:
            return self.seg[idx]
        if high < l and low > r:
            return -sys.maxsize
        mid = (low+high)//2
        left = self.query(2*idx+1,low,mid,l,r)
        right = self.query(2*idx+2,mid+1,high,l,r)
        return max(left,right)
