class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        arr = []
        for num, count in freq.items():
            arr.append([count, num])
        arr.sort()

        out = []
        while len(out) < k:
            out.append(arr.pop()[1])
        return out