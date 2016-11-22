# LeetCode 'Jump Game II' problem

class Solution1(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        # Solution - 1
        """
        length = len(nums)
        index = 0
        longest = 0
        steps = 0
        max = 0
  
        while index < length:
       
           long = index + nums[index]  
           if index <= longest:
               if long > max:
                    max = long
               if index == longest:
                   if longest >= length -1 :
                       return steps
                   longest = max
                   steps += 1 
 
           index += 1
                    
        return steps


class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # Solution - 2 with BFS
        """
        left, right, depth = 0, 0, 0
        
        while right < len(nums)-1:
            left, right, depth = right+1, max( [idx+nums[idx] for idx in range(left, right+1)] ), depth+1 
            
        return depth
        
