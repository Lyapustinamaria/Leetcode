class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        new_arr = []
        
        for i in range(len(arr)):
            if arr[i] == 0:
                new_arr.append(0)
            new_arr.append(arr[i])
                
        for i in range(len(arr)):
            arr[i] = new_arr[i]
                