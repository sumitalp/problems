'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        m = {
            "0": "", "1": "", "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def letterCombinationsRecursion(result, digits, curr, index, m):
            if index==len(digits):
                result.append(curr)
                return
            
            letters = m.get(digits[index])
            
            for i in letters:
                letterCombinationsRecursion(result, digits, curr+i, index+1, m)
            
            
        letterCombinationsRecursion(result, digits, '', 0, m)
        return result
        

ob = Solution()
ob.letterCombinations('23')