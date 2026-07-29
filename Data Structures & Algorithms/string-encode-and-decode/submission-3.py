class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []                        # Create a new list that will be converted to string later
        for s in strs:                  
            res.append(str(len(s)))     # Append the len of the string for decoding later
            res.append("#")             # Using '#' as the delimiter
            res.append(s)               # Append the string
        return "".join(res)             # Return list as a string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
