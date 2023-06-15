class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(len(nums1)-1, m-1, -1):
            nums1.pop(i)

        for i in range(n):
            nums1.append(nums2[i])

        nums1.sort()
