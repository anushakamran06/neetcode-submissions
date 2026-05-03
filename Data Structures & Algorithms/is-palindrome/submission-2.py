class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for l in s:
            if l.isalnum():
                stripped += l
        stripped = stripped.lower() #strings are immutable, need to reassign

        for i in range(len(stripped)):
            if stripped[i] != stripped[-i-1]:
                return False
        return True

#isalnum being used
#0 and -1 
#1 and -2 (-n-1)
#2 and -3