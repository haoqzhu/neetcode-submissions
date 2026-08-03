class Solution:
    def isPalindrome(self, s: str) -> bool:
        validStr = "".join(char for char in s if char.isalnum()).lower()
        print(validStr)
        
        l, r = 0, len(validStr) - 1
        while l < r:
            if validStr[l] != validStr[r]:
                return False
            l += 1
            r -= 1
            
        return True