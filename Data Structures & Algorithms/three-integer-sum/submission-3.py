class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if n > 0:       # if the current number is positive, skip
                break
            if i > 0 and n == nums[i - 1]:
                continue    # skip duplicate numbers
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                target = -n
                sum = nums[l] + nums[r]
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # skip duplicate numbers
                        l += 1
        
        return res
