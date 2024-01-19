class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        start = res = 0
        seen = defaultdict(lambda: -1)

        for i, char in enumerate(s):
            if seen[char] >= start:
                start = seen[char] + 1
            res = max(res, i - start + 1)
            seen[char] = i

        return res
