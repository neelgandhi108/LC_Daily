class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = nums[0]
        for num in nums[1:]:
            res ^= num
        return res