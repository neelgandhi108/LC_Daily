class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used_bits = 0
        window_start = 0
        max_len = 0
        for window_end in range(len(nums)):
            while used_bits & nums[window_end] != 0:
                used_bits ^= nums[window_start] # Remove leftmost bit from left
                window_start += 1 # Remove number from left
            used_bits |= nums[window_end]
            max_len = max(max_len,window_end-window_start+1)
        return max_len