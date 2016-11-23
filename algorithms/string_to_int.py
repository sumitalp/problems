# LeetCode 'String to Int (atoi)' problem

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        sign = '+'
        i= 0
        new_str = ''
        
        if not str:
            return 0
            
        if str[0] == '-':
            sign = '-'
            i = 1
        
        if str[0] == '+':
            i = 1
          
        for j in str[i:]:
            if '9' >= j >= '0':
                new_str += j
            else:
                break
        
        
        if new_str:  
            new_str = sign + new_str
            if int(new_str) >= 2147483648:
                return 2147483647
            elif int(new_str) < -2147483648:
                return -2147483648
            else:
                return int(new_str)
        else:
            return 0
