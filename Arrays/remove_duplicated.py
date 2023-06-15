class Solution:
    def removeDuplicates(self, nums) -> int:

        i = len(nums) - 1

        while i > 0:
            if nums[i] == nums[i-1]:
                nums.pop(i-1)
            i -= 1

        return len(nums)
