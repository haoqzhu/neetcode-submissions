class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "".join(c for c in s if c.isalnum()).lower()

        l, r = 0, len(newStr) - 1
        while l < r:
            if newStr[l] != newStr[r]:
                return False
            l += 1
            r -= 1
        
        return True