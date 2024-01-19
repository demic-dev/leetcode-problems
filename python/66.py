class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        v = reduce(lambda acc, v: (acc * 10) + v, digits)
        v += 1

        return [int(d) for d in str(v)]
