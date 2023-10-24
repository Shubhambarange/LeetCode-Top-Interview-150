# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        while i<n:
            nums1.pop()
            i+=1
        nums1.extend(nums2)
        nums1.sort()
        
        
