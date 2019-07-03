# LeetCode: Median of Two sorted array
# Code Complexity: O(log(m+n))

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)==0 and len(nums2)==0: 
            return 0.0
        
        new_nums = sorted(nums1 + nums2)
        
        # return new_nums[int(len(new_nums)/2)]
        if len(new_nums) % 2 == 1:
            return float( new_nums[int(len(new_nums)/2)] )
        
        return (float( new_nums[int(len(new_nums)/2) - 1] ) + float( new_nums[int(len(new_nums)/2)] )) / 2 
