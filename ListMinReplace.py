class Solution:
    def solve(self, nums):
        min_element = nums[0]
        nums[0] = 0

        for i in range(1, len(nums)):
            if min_element < nums[i]:
                nums[i] = min_element
            elif min_element >= nums[i]:
                temp = nums[i]
                nums[i] = min_element
                min_element = temp
        return nums
