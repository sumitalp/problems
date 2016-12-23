# LeetCode: Longest Substring without repeating characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_repeat = -1
        longest_substr = 0
        positions = {}
        
        for i in range(len(s)):
            if s[i] in positions and last_repeat < positions[s[i]]:
                last_repeat = positions[s[i]]
            if i-last_repeat > longest_substr:
                longest_substr = i-last_repeat
                
            positions[s[i]] = i
        
        return longest_substr         
