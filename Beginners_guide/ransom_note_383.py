class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for char in ransomNote:
            if magazine.find(char) == -1:
                return False
            else:
                magazine = magazine.replace(char, '', 1)

        return True