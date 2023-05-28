class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(nums) - 1):
            i = i + 1
            nums[i] = nums[i] + nums[i-1]

        return nums