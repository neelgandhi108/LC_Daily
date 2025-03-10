import sys
import io
class SegmentTree:
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
        if low >= l and high <= r:
            return self.seg[idx]
        if high < l or low > r:
            return -sys.maxsize
        mid = (low+high)//2
        left = self.query(2*idx+1,low,mid,l,r)
        right = self.query(2*idx+2,mid+1,high,l,r)
        return max(left,right)


def test_segment_tree():
    # Simulated input
    # Number of values
    # Array Values
    # Number of queries
    # Query ranges
    input_data = """5
1 3 2 7 9 
3
0 2
1 4
2 3
"""
    expected_output = """3
9
7
"""

    # Redirect input and output
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()

    # Run the segment tree implementation
    n = int(input())
    arr = list(map(int, input().split()))

    seg_tree = SegmentTree(arr)

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print(seg_tree.query(0, 0, n - 1, l, r))

    # Capture output
    actual_output = sys.stdout.getvalue()

    # Reset standard input/output
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__

    # Assertion for correctness
    assert actual_output == expected_output, f"Expected:\n{expected_output}\nBut got:\n{actual_output}"
    print("Test passed successfully!")


# Run the test case
test_segment_tree()

