class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n , max_cnt = max(nums) , 0
        left = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == max_n:
                max_cnt += 1
            while max_cnt >= k:
                res += (len(nums) - right)
                if nums[left] == max_n:
                    max_cnt -= 1
                left += 1
        return res
