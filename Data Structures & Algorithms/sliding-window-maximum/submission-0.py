class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, k

        while r <= len(nums):
            sub = nums[l:r]
            res.append(max(sub))
            l += 1
            r += 1
        
        return res
            

        


