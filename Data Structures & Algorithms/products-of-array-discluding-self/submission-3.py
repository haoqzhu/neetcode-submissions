class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        res = []
        pre[0] = post[n - 1] = 1
        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1]
        for i in range(n - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
        for i in range(n):
            res.append(pre[i] * post[i])

        return res