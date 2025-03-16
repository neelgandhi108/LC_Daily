class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_count = collections.defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            char_count[s[right]] += 1
            while len(char_count) == 3:
                res += (len(s) - right)
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
        return res
