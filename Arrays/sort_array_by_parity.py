class Solution:
    def sortArrayByParity(self, nums):

        i = len(nums) - 1

        while i >= 0:
            if nums[i] % 2 == 1:
                nums.append(nums[i])
                nums.pop(i)
            i -= 1

        return nums
