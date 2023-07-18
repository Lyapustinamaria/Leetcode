class Solution:
    def findDisappearedNumbers(self, nums):

        not_nums = [i for i in range(1, len(nums)+1)]

        for num in nums:
            index = abs(num) - 1
            not_nums[index] = -abs(not_nums[index])

        return [num for num in not_nums if num > 0]
