class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        reversed_number = 0
        t = x

        while t != 0:
            digit = t % 10
            reversed_number = reversed_number * 10 + digit
            t = t // 10

        return reversed_number == x
