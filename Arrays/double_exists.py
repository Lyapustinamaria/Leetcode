class Solution:
    def checkIfExist(self, arr) -> bool:

        if arr is None:
            return False

        length = len(arr)

        for i in range(length):
            for j in range(length):
                if (i != j and arr[i] == 2 * arr[j]):
                    return True

        return False
