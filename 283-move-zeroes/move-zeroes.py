class Solution:
    def moveZeroes(self,nums):
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                if write != read:
                    nums[write], nums[read] = nums[read], nums[write]
                write += 1
        return nums
