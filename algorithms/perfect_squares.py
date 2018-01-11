# Leetcode problem 279. Perfect Squares

class Solution:
  def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0,1,2,3]
    
    for i in range(4, n+1):
      dp.append(i)
      
      for x in range(1, i+1):
        temp = x*x

        if temp > i:
          break
        else:
          dp[i] = min(dp[i], dp[i-temp] + 1)

    return dp[n]

print(Solution().numSquares(4))

class Solution1:
  _dp = [0]
  def numSquares(self, n):
    dp = self._dp
    while len(dp) <= n:
      dp += min(dp[-i*i] for i in range(1, int(len(dp) ** 0.5+1))) + 1,

    return dp[n]

print(Solution1().numSquares(6))
