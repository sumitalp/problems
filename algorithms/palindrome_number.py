# LeetCode OJ 'Palindrome Number'
import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        if x < 10:
            return True
        """    
        if x < 100:
            return True if x%10 == x//10 else False
  
        digit = 1
        while (x/digit)>9:
            digit *= 10
        """   
        # Find digits of an integer is, int(math.log10(x)) + 1
        # I used only int(math.log10(x)) because I need 0, int(math.log10(x)) times.
        digit = 10**(int(math.log10(x))) 

        while (x!=0):
            start = int(x/digit)
            end   = int(x%10)
            if start != end:
                return False
                
            x = (x % digit) / 10
            digit /= 100
            
        return True
