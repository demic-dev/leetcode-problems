class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrencies = defaultdict(int)

        for i in arr:
            occurrencies[i] += 1

        return len(set(occurrencies.values())) == len(occurrencies)