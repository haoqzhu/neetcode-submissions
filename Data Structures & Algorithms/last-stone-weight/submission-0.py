class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -s)
        
        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            z = -abs(x - y)
            if z < 0:
                heapq.heappush(maxHeap, z)

        return 0 if not maxHeap else -maxHeap[0]
