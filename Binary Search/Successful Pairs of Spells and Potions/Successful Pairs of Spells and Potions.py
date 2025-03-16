class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for spell in spells:
            l , r = 0 , len(potions) - 1
            idx = len(potions)
            while l <= r:
                m = (l+r)//2
                if spell * potions[m] >= success:
                    r = m-1
                    idx = m
                else:
                    l = m+1
            res.append(len(potions)-idx)
        return res