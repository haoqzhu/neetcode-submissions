class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices, values in decreasing order
        res = []

        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Remove indices whose values are smaller than nums[i]
            #    (they can never be the max while nums[i] is still in the window)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Record max once window is full
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
