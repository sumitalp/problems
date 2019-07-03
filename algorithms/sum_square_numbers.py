# LeetCode 633. Sum of Square Numbers

class Solution:
    def is_square(self, N):
        return int(N**.5)**2 == N
    
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        return any(self.is_square(c - a*a) 
                for a in range(int(c**.5) + 1))

print( Solution().judgeSquareSum(4) )