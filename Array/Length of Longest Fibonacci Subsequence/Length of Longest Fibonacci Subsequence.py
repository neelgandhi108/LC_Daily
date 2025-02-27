class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        res = 0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                prev , curr = arr[i]  , arr[j]
                next = prev + curr
                length = 2
                while next in arr_set:
                    length += 1
                    prev , curr = curr, next
                    next = prev+curr
                    res = max(res,length)
        return res