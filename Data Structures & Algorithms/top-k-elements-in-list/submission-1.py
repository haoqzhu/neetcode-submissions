class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        sortedCount = []
        for n, c in count.items():
            sortedCount.append([c, n])
        sortedCount.sort()

        res = []
        while len(res) < k:
            res.append(sortedCount.pop()[1])

        return res