class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        first, last = {}, {}
        count = collections.Counter()
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            count[ch] += 1

        intervals = []
        for ch1, i in first.items():
            for ch2, j in last.items():
                if i <= j:
                    cnt = 0
                    for ch in count:
                        if i <= first[ch] <= last[ch] <= j:
                            cnt += count[ch]
                    if cnt == (j - i + 1) and cnt < len(s):
                        intervals.append((i, j))

        intervals = sorted(intervals, key=lambda x: (x[1] - x[0]))
        res = []
        for i, j in intervals:
            if all(y < i or j < x for x, y in res):
                res.append((i, j))
        return len(res) >= k