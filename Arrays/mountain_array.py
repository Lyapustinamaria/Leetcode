class Solution:
    def validMountainArray(self, arr) -> bool:

        if arr is None:
            return False

        length = len(arr)
        i_max_num = 0

        for i in range(length):
            if arr[i_max_num] < arr[i]:
                i_max_num = i

        if (i_max_num == 0 or i_max_num == length - 1):
            return False

        for i in range(i_max_num):
            if (arr[i] >= arr[i+1]):
                return False

        for i in range(i_max_num, length - 1):
            if (arr[i] <= arr[i+1]):
                return False

        return True
