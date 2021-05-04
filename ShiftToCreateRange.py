class Solution:
    def solve(self, nums):
        n = len(nums)
        idx = nums.index(min(nums))
        return all(nums[(idx+i) % n] == i + 1 for i in range(n)) or all(nums[idx-i] == i+1 for i in range(n))
