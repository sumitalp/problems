'''
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
'''

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if not N or not K:
            return
        
        rows = ['0']
        def kthGrammarRecursive(rows, N, index):
            if index==N:
                return
            
            letters = rows[index]
            st = ''
            for l in letters:
                st += '01' if l=='0' else '10'
                    
            rows.append(st)
            
            kthGrammarRecursive(rows, N, index+1)
            
        kthGrammarRecursive(rows, N, 0)
        return rows[N-1][K-1]
        
if __name__=='__main__':
    ob = Solution()
    ob.kthGrammar(4,5) # Output: 1
    ob.kthGrammer(30, 2**29) # Time limit exceeded

'''
Below solution using Thue-Morse algorithm

The Thue-Morse sequence may be obtained recursively by appending the bitwise negative (ones' complement) of the string to itself. So, we can iteratively remove the first binary digit from K and negate our answer.

(This is equivalent to counting number of 1s in the binary expansion of K, but it appears to be faster due to Python's bin() command being less optimized for speed).
'''
class Solution2:
    def kthGrammar(self, N: int, K: int) -> int:
	return abs(K-1) if K<=2 else 1-self.kthGrammar(N-1, K-(1<<int(log2(K-1))))
