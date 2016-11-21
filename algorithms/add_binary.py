# LeetCode 'Add Two Binary' problem

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = self.binStrToInt(a)
        b = self.binStrToInt(b)
        
        return bin(a+b)[2:]
        
    def binStrToInt(self, binary_str):

        """The function binStrToInt() takes in one input, a string of ones and
        zeros (no spaces) called BINARY_STR.  It treats that input as a binary
        number (base 2) and converts it to a decimal integer (base 10). It
        returns an integer result."""
    
        length = len(binary_str)
    
        num = 0
        for i in range(length):
            num = num + int(binary_str[i])
            num = num * 2
        return num / 2
