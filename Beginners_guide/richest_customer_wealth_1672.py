class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m = len(accounts)
        n = len(accounts[0])
        finalSum = 0

        for i in range(m):

            currentSum = 0

            for j in range(n):
                currentSum = currentSum + accounts[i][j]
            if currentSum > finalSum:
                finalSum = currentSum
        
        return finalSum
