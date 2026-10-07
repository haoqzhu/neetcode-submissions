class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for n, c in count.items():
            heapq.heappush(heap, [-c, n])
        
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res