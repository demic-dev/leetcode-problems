class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        hi = len(nums) - 1
        while(low <= hi):
            mid = (low+hi)//2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                return mid

        return low