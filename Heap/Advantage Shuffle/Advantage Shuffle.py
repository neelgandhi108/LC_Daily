class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        res = [0]*len(nums1)
        heap = [(-nums2[i],i) for i in range(len(nums2))]
        heapq.heapify(heap)
        low , high = 0 , len(nums1) - 1
        while low <= high:
            val , idx = heapq.heappop(heap)
            val = -val
            if val < nums1[high]:
                res[idx] = nums1[high]
                high -= 1
            else:
                res[idx] = nums1[low]
                low += 1
        return res