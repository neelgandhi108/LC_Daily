class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev , next = 0 , 0
        total = 0
        for row in bank:
            one_count = row.count("1")
            if one_count:
                next = one_count
                total += prev*next
                prev = next
        return total