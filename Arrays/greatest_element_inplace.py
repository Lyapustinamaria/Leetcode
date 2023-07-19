class Solution:
    def replaceElements(self, arr):

        i = len(arr) - 1
        max_replace = -1

        while i >= 0:
            if arr[i] > max_replace:
                max_replace, arr[i] = arr[i], max_replace
            else:
                arr[i] = max_replace
            i -= 1

        return arr
