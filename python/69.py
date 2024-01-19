class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        low = 0
        hi = x
        while low <= hi:
            mid = (low + hi) // 2
            if mid*mid > x:
                hi = mid - 1
            elif mid*mid < x:
                low = mid + 1
            else:
                return mid

        return hi