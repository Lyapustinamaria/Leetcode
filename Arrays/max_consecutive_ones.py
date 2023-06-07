# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        
        max_len = 0
        count = 0
        
        for num in nums:
            if num == 1:
                count += 1
                max_len = max(max_len, count)
            else:
                count = 0
        return max_len