class Solution:
    def sortedSquares(self, nums):
        
        squares = []

        for num in nums:
            squares.append(num ** 2)
    
        squares.sort()
        
        return squares