class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            vowel_dict = collections.defaultdict(int)
            consonant_count = 0
            res = 0
            l = 0
            for r in range(len(word)):
                if word[r] in "aeiou":
                    vowel_dict[word[r]] += 1
                else:
                    consonant_count += 1
                while len(vowel_dict) == 5 and consonant_count >= k:
                    res += (len(word) - r)
                    if word[l] in "aeiou":
                        vowel_dict[word[l]] -= 1
                        if vowel_dict[word[l]] == 0:
                            del vowel_dict[word[l]]
                    else:
                        consonant_count -= 1
                    l += 1
            return res

        return atleastk(k) - atleastk(k + 1)

