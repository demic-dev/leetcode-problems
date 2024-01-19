class Solution:
    results = defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n in self.results:
            return self.results[n]
        
        self.results[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.results[n]
