class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        res = 0
        q = deque() # Pairs of [-cnt, idleTime]

        while maxHeap or q:
            res += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, res + n])
            if q and q[0][1] == res:
                temp = q.popleft()
                heapq.heappush(maxHeap, temp[0])
        return res