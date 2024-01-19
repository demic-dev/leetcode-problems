class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack.find(needle) == -1:
            return -1
        else:
            return haystack.index(needle)
