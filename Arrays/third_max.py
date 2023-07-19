class Solution:
    def thirdMax(self, nums) -> int:

        nums.sort(reverse=True)

        third_max_num = nums[0]
        iterator = 1

        for i in range(len(nums)):
            if third_max_num > nums[i]:
                third_max_num = nums[i]
                iterator += 1

            if iterator == 3:
                break

        if iterator < 3:
            third_max_num = nums[0]

        return third_max_num
