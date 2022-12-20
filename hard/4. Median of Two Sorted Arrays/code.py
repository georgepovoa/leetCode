class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = sorted(nums1 + nums2) 
        
        mid = len(result)/2
        
        if int(mid)!= mid:
            return result[len(result)//2]
        else:
            return (result[int(mid)] + result[int(mid-1)]) / 2
        