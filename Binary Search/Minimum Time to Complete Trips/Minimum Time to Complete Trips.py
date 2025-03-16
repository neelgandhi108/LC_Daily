class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left , right = 1, max(time)*totalTrips
        res = -1
        while left <= right:
            mid = (left+right)//2
            countTrips = 0
            for t in time:
                countTrips += math.floor(mid/t)
            if countTrips >= totalTrips:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res