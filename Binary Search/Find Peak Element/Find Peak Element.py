class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search(l,r):
            if l == r:
                return l
            mid = l + (r-l) // 2
            if nums[mid] > nums[mid+1]:
                return binary_search(l,mid)
            return binary_search(mid+1,r)
        return binary_search(0,len(nums)-1)