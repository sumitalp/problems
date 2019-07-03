# LeetCode OJ 'Reverse Integer Problem'

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos_or_neg = 1
        result = 0
        
        if x < 0:
            pos_or_neg = -1
            
        x = abs(x)

        while x > 0:
            result *= 10
            result += (x%10)
            x /= 10
        
        if -2147483647 < result < 2147483647:
            return int(result * pos_or_neg)
        else:
            return 0
