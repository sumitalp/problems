'''
16. 3Sum Closest
Medium

4806

222

Add to List

Share
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''

# Approach: Two pointer
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if nums.count(0) == len(nums): return 0
        closest = float('inf')
        nums.sort()
        
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) - 1
            
            while left<right:
                sm = nums[i] + nums[left] + nums[right]
                
                if abs(target-sm) < abs(target-closest):
                    closest = sm
                
                if sm > target:
                    right -= 1
                else:
                    left += 1
        
        return closest
