class Solution:
    def greatestLetter(self, s: str) -> str:
        greatest_letter = ""

        for char in s:
            upper_char = char.upper()

            if upper_char != char and upper_char in s:
                if not greatest_letter or upper_char > greatest_letter:
                    greatest_letter = upper_char

        return greatest_letter
