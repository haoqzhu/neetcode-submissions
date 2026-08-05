class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for s in s1:
            freq[s] = freq.get(s, 0) + 1
        
        l, r = 0, len(s1) - 1
        while r < len(s2):
            subfreq = {}
            for s in range(l, r + 1):
                subfreq[s2[s]] = subfreq.get(s2[s], 0) + 1
            
            if subfreq == freq:
                return True
            l += 1
            r += 1
        return False