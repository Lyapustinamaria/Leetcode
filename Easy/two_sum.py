class Solution:

    def twoSum(self, nums, target: int):
        # Time: O(n^2)
        # Space: O(1)
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    def twoSum_1(self, nums, target: int):
        # Time: O(n)
        # Space: O(n)

        numMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]

            numMap[nums[i]] = i
