class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        t_freq, window = defaultdict(int), defaultdict(int)
        for i in t:
            t_freq[i] = t_freq.get(i, 0) + 1

        have, need = 0, len(t_freq)
        res, resLen = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in t_freq and window[c] == t_freq[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1
                
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""
