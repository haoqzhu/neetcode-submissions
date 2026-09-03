class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = nums1 + nums2
        new.sort()
        length = len(new)
        if length % 2 == 0:
            return (new[length // 2] + new[length // 2 - 1]) / 2.0
        else:
            return new[length // 2]
        return - 1