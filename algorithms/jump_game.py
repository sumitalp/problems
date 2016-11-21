# LeetCode 'Jump Game' problem

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
                
            if max_reach < i+nums[i]:
                max_reach = i+nums[i]
                
        return True
