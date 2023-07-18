class Solution:
    def heightChecker(self, heights) -> int:

        count = 0
        expected = heights.copy()

        expected.sort()

        for i in range(len(expected)):
            if expected[i] != heights[i]:
                count += 1

        return count
