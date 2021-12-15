'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000


Algorithm
If the array is empty, return 0
If the array has just one element, return that element
Create a function robLinear() that returns the maximum sum that can be obtained in a linear array
robLinear() works as follows:
Initiate two variables included and excluded as 0, which stores the max results that be obtained by including and excluding the current element respectively
At every next iteration, included becomes the current element + excluded result of previous element
Excluded becomes the maximum of included and excluded results of previous element
Return the maximum of robLinear(1 , N – 1) and robLinear(2 , N)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        def helper(left:int, right:int, arr:list):
            inc, exc, cur = 0, 0, 0
            for i in range(left, right):
                cur = max(inc, exc)
                inc = exc + arr[i]
                exc = cur
                
            return max(inc, exc)
        
        return max(helper(0, len(nums)-1, nums), helper(1, len(nums), nums))

if __name__=="__main__":
  print(Solution.rob([1,2,1,1])) # 3
  print(Solution.rob([2,3,2])) # 3
